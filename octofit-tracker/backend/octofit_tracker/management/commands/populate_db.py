from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Clear existing data in child-to-parent order (delete individually to avoid Djongo issues)
        for obj in Leaderboard.objects.all():
            obj.delete()
        for obj in Activity.objects.all():
            obj.delete()
        for obj in Workout.objects.all():
            obj.delete()
        for obj in User.objects.all():
            obj.delete()
        for obj in Team.objects.all():
            obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel),
            User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel),
            User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc),
            User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength training', difficulty='Hard'),
            Workout.objects.create(name='Flight Training', description='Aerobic exercise', difficulty='Medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Strength', duration=60, date=timezone.now())
        Activity.objects.create(user=users[1], type='Cardio', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], type='Stealth', duration=30, date=timezone.now())
        Activity.objects.create(user=users[3], type='Flight', duration=50, date=timezone.now())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
