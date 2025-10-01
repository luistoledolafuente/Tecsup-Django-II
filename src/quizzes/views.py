from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Quiz, Question, Choice
from .serializers import (
    QuizSerializer, QuestionSerializer, ChoiceSerializer,
    QuizDetailSerializer, SubmitAnswerSerializer
)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': 'Quiz API v1',
        'endpoints': {
            'quizzes': reverse('quiz-list', request=request, format=format),
            'questions': reverse('question-list', request=request, format=format),
            'choices': reverse('choice-list', request=request, format=format),
        }
    })

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer
    
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        quiz = self.get_object()
        serializer = SubmitAnswerSerializer(data=request.data.get('answers', []), many=True)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        answers = serializer.validated_data
        results = []
        correct_count = 0
        
        for answer in answers:
            try:
                question = Question.objects.get(id=answer['question_id'], quiz=quiz)
                choice = Choice.objects.get(id=answer['choice_id'], question=question)
                
                is_correct = choice.is_correct
                if is_correct:
                    correct_count += 1
                
                results.append({
                    'question_id': question.id,
                    'question_text': question.text,
                    'choice_id': choice.id,
                    'choice_text': choice.text,
                    'is_correct': is_correct
                })
            except (Question.DoesNotExist, Choice.DoesNotExist):
                results.append({
                    'question_id': answer['question_id'],
                    'error': 'Invalid question or choice'
                })
        
        total = len(results)
        percentage = round((correct_count / total) * 100, 2) if total > 0 else 0
        
        grade_map = {
            90: ('A', '🏆'),
            80: ('B', '🎉'),
            70: ('C', '👍'),
            60: ('D', '📚'),
            0: ('F', '💪')
        }
        
        grade, emoji = next((g, e) for threshold, (g, e) in sorted(grade_map.items(), reverse=True) if percentage >= threshold)
        
        return Response({
            'quiz_id': quiz.id,
            'quiz_title': quiz.title,
            'total_questions': total,
            'correct_answers': correct_count,
            'score': f"{correct_count}/{total}",
            'percentage': percentage,
            'grade': grade,
            'emoji': emoji,
            'results': results
        })