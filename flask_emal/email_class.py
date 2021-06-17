#-*- coding: UTF-8 -*-

from pyMail import pyMail
server_imap = "imap.qq.com"
server_smtp = "smtp.qq.com"


class Email_info:
    def __init__(self,username,password):
        # 暂时写死qq邮箱部分 ，后续可以通过username来进行判断
        self.email = pyMail.ReceiveMailDealer(username,password,server_imap)
        self.email.select('INBOX')
        self.email_send = pyMail.SendMailDealer(username,password,server_smtp)
    def get_unread(self):
        return self.email.getUnread()
    def detail(self,num):
        return self.email.getMailInfo_all(num)
    def detail2(self,num):
        self.email.select("Sent Messages")
        mess = self.email.getMailInfo_all(num)
        self.email.select("INBOX")
        return mess
    def show_folder(self):
        return self.email.showFolders()
    def traversal_unread(self):
        list_subject = []
        num_list = []

        real_Unseen = self.email.getUnread_real()[1][0].split(' ')
        for num in self.email.getUnread()[1][0].split(' ')[-30:][::-1]:
            # print(len(num))
            if num != '':
                mailInfo = self.email.getMailInfo(num)
                print mailInfo['subject']
                num_list.append(num)
                list_subject.append(mailInfo['subject'].decode("utf-8"))
                # print mailInfo['body']
                # print mailInfo['html']
                # print mailInfo['from']
                # print mailInfo['to']
                # 遍历附件列表
                # for attachment in mailInfo['attachments']:
                #     fileob = open(attachment['name'], 'wb')
                #     fileob.write(attachment['data'])
                #     fileob.close()
        return list_subject,num_list,real_Unseen

    def traversal_Send(self):
        list_subject = []
        num_list = []
        self.email.select("Sent Messages")
        real_Unseen = self.email.getUnread_real()[1][0].split(' ')
        for num in self.email.getSend()[1][0].split(' ')[-30:][::-1]:
            # print(len(num))
            if num != '':
                mailInfo = self.email.getMailInfo(num)
                print mailInfo['subject']
                num_list.append(num)
                list_subject.append(mailInfo['subject'].decode("utf-8"))
                # print mailInfo['body']
                # print mailInfo['html']
                # print mailInfo['from']
                # print mailInfo['to']
                # 遍历附件列表
                # for attachment in mailInfo['attachments']:
                #     fileob = open(attachment['name'], 'wb')
                #     fileob.write(attachment['data'])
                #     fileob.close()
        self.email.select("INBOX")

        return list_subject,num_list,real_Unseen
    def send_email(self,to_address,title,txt_html,file_list):

        self.email_send.setMailInfo(to_address,title,txt_html,"html",file_list)
        self.email_send.sendMail()
