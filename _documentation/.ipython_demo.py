import django, os
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newspaper.settings")
django.setup()

from demo.models import Reporter, Article

Reporter.objects.all()
r = Reporter(full_name="Deep Thought")
r.save()

Reporter.objects.all()
r.delete()

Reporter.objects.count()

for number in range(1..10):
    new_reporter = Reporter(full_name = 'No. {}'.format(number))
    new_reporter.save()

# Delete all reporter
for reporter in Reporter.objects.all():
    print(reporter.full_name)
    reporter.delete()
