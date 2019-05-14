import time
import os
import io
import datetime
import logging
import sys
import zipfile
from zipfile import ZipFile

import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(send_to, subject, attachment, 
    send_from='abc@gmail.com', 
    server='smtp.gmail.com', 
    port='587', 
    username='abc@gmail.com', 
    password='abcabcabc'):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = subject

    ctype, encoding = mimetypes.guess_type(attachment)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)
    with open(attachment) as fhandle:
        attachment = MIMEText(fhandle.read(), _subtype=subtype)

    attachment.add_header("Content-Disposition", "attachment", attachment=attachment)
    msg.attach(attachment)

    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)

    formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    streamhandler = logging.StreamHandler(sys.stdout)
    streamhandler.setFormatter(formatter)
    filehandler = logging.FileHandler('{}.log'.format(logger_name))
    filehandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(streamhandler)
    logger.addHandler(filehandler)

    return logger


def timer(input_func):

    def wrapper(*args, **kwargs):
        ti = time.time()
        input_func(*args, **kwargs)
        print('\n time taken by the function to run ==> {:.2f} mins \n'.format((time.time() - ti)/60))

    return wrapper


def create_timedir(path):
    timedir = str(datetime.datetime.today().strftime('%Y%m%d%H%M'))
    if not os.path.exists(os.path.join(path, timedir)):
        os.makedirs(os.path.join(path, timedir))

    return os.path.join(path, timedir)


def clear_dir(dirpath):
    if os.path.isdir(dirpath)
        shutil.rmtree(dirpath)
        
    os.makedirs(dirpath)


def compress_file(dataframe, dirpath, document):
    with ZipFile('{}/{}.zip'.format(dir_path, document), 'w', zipfile.ZIP_DEFLATED) as z:
        string_buffer = io.StringIO()
        dataframe.loc[:, display_feats].to_csv(string_buffer, index=False)
        z.writestr('{}'.format(document), string_buffer.getvalue())






