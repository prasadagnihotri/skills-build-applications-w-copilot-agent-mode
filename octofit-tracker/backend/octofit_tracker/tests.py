from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertIsNotNone(team.id)
    def test_user_create(self):
        team = Team.objects.create(name='Test Team2', description='desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertIsNotNone(user.id)
    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertIsNotNone(workout.id)
    def test_activity_create(self):
        team = Team.objects.create(name='Test Team3', description='desc')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Cardio', duration=30, date='2025-01-01')
        self.assertIsNotNone(activity.id)
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team4', description='desc')
        user = User.objects.create(name='Test User3', email='test3@example.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=100)
        self.assertIsNotNone(lb.id)
