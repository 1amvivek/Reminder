from .models import TaskList, Task
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .forms import AddTaskList, AddTask, FeedbackForm
from django.utils import timezone
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from twilio.rest import TwilioRestClient
from celery.decorators import task
from datetime import datetime, timedelta



# Create your views here.


def list(request):
    tasks = Task.objects.all().order_by("id")
    taskLists = TaskList.objects.all()
    return render(request, 'Notify/view.html', {'tasks': tasks, 'taskLists': taskLists})



def task_card_delete(request, pk):
    tasklist = get_object_or_404(TaskList, pk=pk)
    tasklist.delete()
    return redirect('../')



def task_add_list(request):
    if request.method == 'POST':
        form = AddTaskList(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = AddTaskList()
    return render(request, 'Notify/add_list.html', {'form': form})


def add_task(request):
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            # print('post.reminder')
            # time = post.reminder
            # send_sms.apply_async(eta=post.reminder)
            msg = 'You are being reminded of a task:' + post.summary +' at '+ str(post.reminder) + '--from Notify Team.'
            send_sms(msg)
            return redirect('../')
    else:
        form = AddTask()
    return render(request, 'Notify/add.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/')


def feedback(request):
    form_class = FeedbackForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = Context({'contact_name': contact_name,'contact_email': contact_email,'form_content': form_content,})
        content = template.render(context)

        email = EmailMessage(
            "Feedback form submission",
            content,
            "viveklakshmanan@live.com" + '',
            ['vivekthesmart@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('../')

    return render(request, 'Notify/feedback_form.html', {'form': form_class, })



# @task(name="send_sms")
def send_sms(msg):
    account_sid = 'ACd540203503f84c32e8b046b2e372e691'
    auth_token = '451951ff2fe8b6101e3f53838ca4207a'
    my_cell = '+16692924707'
    my_twilio = '+16692010306'
    client = TwilioRestClient(account_sid, auth_token)

    client.messages.create(
        body=msg,
        to=my_cell,
        from_=my_twilio,
        )