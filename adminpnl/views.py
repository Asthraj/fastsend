from django.shortcuts import render,redirect
import pandas as pd
from django.urls import reverse
from .forms import DocumentForm
from .models import Document
import json
from django.contrib import messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from twilio.rest import Client
def backtohome(request):
        return redirect(reverse("home"))
def exportmail(request):
    text = "This is the content of my text file."
    file_path = os.path.join(settings.MEDIA_ROOT, 'mytextfile.txt')
    with open(file_path, 'w') as file:
        file.write(text)
    email = EmailMessage(
        'Text file attachment',
        'Please find the attached text file',
        'surajmishra7566@gmail.com',
        ['surajmishra7566@gmail.com'],
    )
    email.attach_file(file_path)
    email.send()
    return HttpResponse('Email sent successfully')
def adminhome(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username != "Admin" or password != "Suraj@123":
                return render(request, 'index.html', {'error': 'Invalid username or password'})
            request.session['my_var'] = username
            return render(request, 'adminpnl/adminhome.html')
        my_value = request.session['my_var']
        print(my_value)
        if my_value is not None:
                username=my_value
                return render(request, 'adminpnl/adminhome.html')
        else:
            return render(request, 'index.html', {'error': 'Please login to continue...'})
    except:
        return render(request, 'index.html', {'error': 'Please login to continue...'})
def logout(request):
    request.session['my_var']= None
    return redirect(reverse('index'))
def myview(request):
    my_value = request.session.get('my_var')
    print(my_value)

    if my_value is not None:
        methd = request.GET.get('q')
        print(methd)
        message = 'Select only excel sheet to import contacts'
        # Handle file upload
        if request.method == 'POST':

            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'])
                # newdoc.save()
                file = request.FILES['docfile']
                print("done1")
                df = pd.read_excel(file)
                df["sno"] = list(range(1, len(df.index) + 1))
                settings.MY_DF = df
                json_records = df.reset_index().to_json(orient='records')
                data = []
                data = json.loads(json_records)
                context = {'d': data}
                print("error just before session")
                request.session['file_data'] = data
                print(df)
                print("done")
                return render(request, 'showdata.html', context)
                # Redirect to the document list after POST

            else:
                message = 'The form is not valid. Fix the following error:'
        else:
            form = DocumentForm()  # An empty, unbound form

        # Load documents for the list page
        documents = Document.objects.all()

        # Render list page with the documents and the form
        context = {'documents': documents, 'form': form, 'message': message}
        return render(request, 'list.html', context)
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})
def myviewe(request):
    my_value = request.session.get('my_var')
    print(my_value)

    if my_value is not None:
        methd = request.GET.get('q')
        print(methd)
        message = 'Select only excel sheet to import contacts to export contacts to the device'
        # Handle file upload
        if request.method == 'POST':

            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'])
                # newdoc.save()
                file = request.FILES['docfile']
                print("done1")
                df = pd.read_excel(file)
                df["sno"] = list(range(1, len(df.index) + 1))
                settings.MY_DF = df
                json_records = df.reset_index().to_json(orient='records')
                data = []
                data = json.loads(json_records)
                context = {'d': data}
                print("error just before session")
                request.session['file_data'] = data
                print(df)
                print("done")
                return render(request, 'showdatae.html', context)
                # Redirect to the document list after POST

            else:
                message = 'The form is not valid. Fix the following error:'
        else:
            form = DocumentForm()  # An empty, unbound form

        # Load documents for the list page
        documents = Document.objects.all()

        # Render list page with the documents and the form
        context = {'documents': documents, 'form': form, 'message': message}
        return render(request, 'liste.html', context)
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})
def myvieww(request):
    my_value = request.session.get('my_var')
    print(my_value)

    if my_value is not None:
        methd = request.GET.get('q')
        print(methd)

        message = 'Select only excel sheet to import contacts \n Send message to whatsapp'
        # Handle file upload
        if request.method == 'POST':

            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'])
                # newdoc.save()
                file = request.FILES['docfile']
                print("done1")
                df = pd.read_excel(file)
                df["sno"] = list(range(1, len(df.index) + 1))
                settings.MY_DF = df
                json_records = df.reset_index().to_json(orient='records')
                data = []
                data = json.loads(json_records)
                context = {'d': data}
                print("error just before session")
                request.session['file_data'] = data
                print(df)
                print("done")
                return render(request, 'whatsappshowdata.html', context)
                # Redirect to the document list after POST

            else:
                message = 'The form is not valid. Fix the following error:'
        else:
            form = DocumentForm()  # An empty, unbound form

        # Load documents for the list page
        documents = Document.objects.all()

        # Render list page with the documents and the form
        context = {'documents': documents, 'form': form, 'message': message}
        return render(request, 'wlist.html', context)
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})
def myviewt(request):
    my_value = request.session.get('my_var')
    print(my_value)

    if my_value is not None:
        methd = request.GET.get('q')
        print(methd)

        message = 'Select only excel sheet to import contacts to send text message'
        # Handle file upload
        if request.method == 'POST':

            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'])
                # newdoc.save()
                file = request.FILES['docfile']
                print("done1")
                df = pd.read_excel(file)
                df["sno"] = list(range(1, len(df.index) + 1))
                settings.MY_DF = df
                json_records = df.reset_index().to_json(orient='records')
                data = []
                data = json.loads(json_records)
                context = {'d': data}
                print("error just before session")
                request.session['file_data'] = data
                print(df)
                print("done")
                return render(request, 'txtshowdata.html', context)
                # Redirect to the document list after POST

            else:
                message = 'The form is not valid. Fix the following error:'
        else:
            form = DocumentForm()  # An empty, unbound form

        # Load documents for the list page
        documents = Document.objects.all()

        # Render list page with the documents and the form
        context = {'documents': documents, 'form': form, 'message': message}
        return render(request, 'tlist.html', context)
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})

def file_operations(request):
    my_value = request.session.get('my_var')
    print(my_value)
    if my_value is not None:
        if request.method == 'POST':
            file = request.FILES('file')
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'])
                newdoc.save()
                print("successful")
            print(file)
            print("file uploaded")
            filename = r"{}".format(file)
            df = pd.read_excel(filename)
            print(df.index)
            data = df
            json_records = df.reset_index().to_json(orient='records')
            data = []
            data = json.loads(json_records)
            context = {'d': data}
            stats=[]
            df["status"] = []
            column = data
            s = ""
            begin = "BEGIN:VCARD\nVERSION:2.1"

            for i in range(len(column)):
                if str(column["Phone"][i]) in request.POST:
                    stats.append(1)
                else:
                    stats.append(0)
                fName = ""
                secMail = ""
                status = ""
                if (str(column["Phone"][i]) != "nan"):
                    if (str(column["Name"][i]) != "nan"):
                        fName = str(column["Name"][i])
                    secN = "\nN:" + fName + ";;;"
                    secPhone = "\nTEL;CELL:+91" + str(column["Phone"][i]).split(".")[0]
                    if ("Mail" in column.columns.values):
                        secMail = ""
                        if (str(column["Mail"][i]) != "nan"):
                            secMail = "\nEMAIL;HOME:" + str(column["Mail"][i])
                    if (column["status"][i]) == 1:
                        s += begin + secN + secPhone + secMail + "\nEND:VCARD\n"
            print(s)
            print(stats)
            # return render(request, 'adminpnl/showdata.html', {'dataframe': df})
            return render(request, 'adminpnl/showdata.html')
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})

def uploadfile(request):
    my_value = request.session.get('my_var')
    print(my_value)

    if my_value is not None:
        return render(request,"testu.html")
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})
def showdata(request):
    if request.method =="POST":
        filedata = request.session.get('file_data', None)
        print(filedata)
        checked_value= request.POST.getlist("check_box")
        print(checked_value)
        df= pd.DataFrame(filedata['df'])
        print(df)
        values=[]
        for i in filedata:
            # if [i.Phone] in request.POST:
            # value = request.POST.get("Phone")
            # print(value)
            # value.append(values)
            print(["Phone"][i])
        print("ho gya bs")
        return redirect("showdata")
    filedata=request.session.get('file_data',None)
    if filedata:
        print(filedata)
    data=settings.MY_DF
    print('data')
    print(settings.MY_DF)
    print("hello world")
    return render(request,"showdata.html")
def dataexport(request):
    my_value = request.session.get('my_var')
    print(my_value)

    if my_value is not None:
        data = settings.MY_DF
        print(data)
        suff = request.POST.get('suff')
        column = data
        stats = []
        for i in range(len(column)):
            if str(column["Phone"][i]) in request.POST:
                stats.append(1)
            else:
                stats.append(0)
        data["status"] = stats
        s = ""
        begin = "BEGIN:VCARD\nVERSION:2.1"

        for i in range(len(column)):
            fName = ""
            secMail = ""
            status = ""
            if (str(column["Phone"][i]) != "nan"):
                if (str(column["Name"][i]) != "nan"):
                    fName = str(column["Name"][i])
                secN = "\nN:" +suff+ fName + ";;;"
                secPhone = "\nTEL;CELL:+91" + str(column["Phone"][i]).split(".")[0]
                if ("Mail" in column.columns.values):
                    secMail = ""
                    if (str(column["Mail"][i]) != "nan"):
                        secMail = "\nEMAIL;HOME:" + str(column["Mail"][i])
                if (column["status"][i]) == 1:
                    s += begin + secN + secPhone + secMail + "\nEND:VCARD\n"
        print(stats)
        from django.http import HttpResponse

        response = HttpResponse(s, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="exported_contact.vcf"'
        return response
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})
def export_to_mail(request):
    my_value = request.session.get('my_var')
    print(my_value)

    if my_value is not None:
        try:
            rmail = request.POST.get('fname')
            suff = request.POST.get('suff')
            rmail = rmail.split(",")
            mail_content = request.POST.get("body")
            # The mail addresses and password
            sender_address = 'info.praedicoglobalresearch@gmail.com'
            sender_pass = 'resfrjklhdbphxnw'
            print(rmail)
            receiver_address = rmail
            # Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = ", ".join(receiver_address)
            message['Subject'] = request.POST.get('subject')
            # The subject line
            # The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))

            data = settings.MY_DF
            print(data)
            stats=[]

            column = data
            stats = []
            for i in range(len(column)):
                if str(column["Phone"][i]) in request.POST:
                    stats.append(1)
                else:
                    stats.append(0)
            data["status"] = stats

            s = ""
            begin = "BEGIN:VCARD\nVERSION:2.1"

            for i in range(len(column)):

                fName = ""
                secMail = ""
                status = ""
                if (str(column["Phone"][i]) != "nan"):
                    if (str(column["Name"][i]) != "nan"):
                        fName = str(column["Name"][i])
                    secN = "\nN:" + suff + fName + ";;;"
                    secPhone = "\nTEL;CELL:+91" + str(column["Phone"][i]).split(".")[0]
                    if ("Mail" in column.columns.values):
                        secMail = ""
                        if (str(column["Mail"][i]) != "nan"):
                            secMail = "\nEMAIL;HOME:" + str(column["Mail"][i])
                    if (column["status"][i]) == 1:
                        s += begin + secN + secPhone + secMail + "\nEND:VCARD\n"
            print(stats)
            file_path = os.path.join(settings.MEDIA_ROOT, 'mytextfile.vcf')
            with open(file_path, 'w') as file:
                file.write(s)
            attach_file_name = 'newcont.vcf'
            attach_file = open(file_path, 'rb')  # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream', name=os.path.basename("mycont.vcf"))
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)  # encode the attachment
            # add payload header with filename
            payload.add_header('Content-Decomposition', 'attachment', filename="mycont.vcf")
            message.attach(payload)
            # Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
            session.starttls()  # enable security
            session.login(sender_address, sender_pass)  # login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent Successfully')
            return render(request, "complete.html")
        except:
            return redirect(reverse(myview))
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})

def sendsms(request):
    my_value = request.session.get('my_var')
    print(my_value)

    if my_value is not None:
        account_sid = 'AC439af5efeef2bea045d7fbbdbedd27d3'
        auth_token = '81726d82eb0c151ed177b351e7c912e2'
        client = Client(account_sid, auth_token)
        data = settings.MY_DF
        print(data)

        column = data
        stats = []
        for i in range(len(column)):
            if str(column["Phone"][i]) in request.POST:
                stats.append(1)
            else:
                stats.append(0)
        data["status"] = stats
        phoneno = []

        print("tastdone")
        for i in range(len(column)):
            fName = ""
            secMail = ""
            status = ""
            if (str(column["Phone"][i]) != "nan"):
                if (str(column["Name"][i]) != "nan"):
                    fName = str(column["Name"][i])
                secN = "\nN:" + fName + ";;;"
                secPhone = "+91" + str(column["Phone"][i]).split(".")[0]
                if str(column["Phone"][i]) in request.POST:
                    phoneno.append(secPhone)
        print(phoneno)
        msgbody = request.POST.get('message')
        print(msgbody)
        for i in phoneno:
            message = client.messages.create(
                messaging_service_sid='MG3fd1368f1ef7561c0b6e68bdcac2df9c',
                body=msgbody,
                to=i
            )
        print(message.sid)
        print("message send successfully")

        return render(request, "completet.html")
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})

def sendwhatsapp(request):
    my_value = request.session.get('my_var')
    print(my_value)
    if my_value is not None:
        account_sid = 'AC439af5efeef2bea045d7fbbdbedd27d3'
        auth_token = '81726d82eb0c151ed177b351e7c912e2'
        client = Client(account_sid, auth_token)
        data = settings.MY_DF
        column = data
        phoneno = []
        for i in range(len(column)):
            fName = ""
            secMail = ""
            status = ""
            if (str(column["Phone"][i]) != "nan"):
                if (str(column["Name"][i]) != "nan"):
                    fName = str(column["Name"][i])
                secN = "\nN:" + fName + ";;;"
                secPhone = "+91" + str(column["Phone"][i]).split(".")[0]
                if str(column["Phone"][i]) in request.POST:
                    phoneno.append(secPhone)
        print(phoneno)
        msgbody = request.POST.get('message')
        for i in phoneno:
            no ='whatsapp'+str(i)
            print("send message to ",no)
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=msgbody,
                to=no
            )
        print(message.sid)
        messages.info(request, "message sent successfully")
        print("message sent successfully")
        return render(request, "completew.html")
    else:
        return render(request, 'index.html', {'error': 'Please login to continue...'})

