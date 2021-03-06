from O365 import Account
import os
# O365-Client -- A client to connect O365
# Copyright (C) 2020  Micraow

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
credentials = ('74424fcf-55d7-4e15-99d7-1663c0ba2e94',)
account = Account(credentials, auth_flow_type='public')
class mailbox_actions:
    """用来对邮箱进行操作"""

    def __init__(self, choice=None, to_who=None, subj=None, text=None):

        # 已实现公共客户端流
        self.account = account
        self.credentials = credentials
        self.choice = choice
        self.scopes = ['basic', 'message_all']  # 请求权限
        self.to_who = to_who
        self.subj = subj
        self.text = text

    def check_if_authenticated(self):
        """检查是否有用户登录，若无，则请求登录"""
        if not self.account.is_authenticated:  # 检查是否登录
            # 请求登录
            self.account.authenticate(scopes=self.scopes)

    def read_email(self):
        """遍历邮件
        limit 表示加载多少个，微软官方一次API调用只返回999个，
        而O365模块默认25个，只有limit>25时utils分页功能才生效
        batch批处理表示加载多少次，就是往后加载
        limit=2000, batch=10 = limit=2000
        但是分为10次加载。"""

        mailbox = self.account.mailbox()
        print('''
        你要进入哪个文件夹？
        1.收件箱
        2.已发送
        3.垃圾邮件
        4.已删除\n
        ''')  # 选择进入哪个文件夹
        readbox = input('请输入对应数字')

        if readbox == '1':
            readbox = mailbox.inbox_folder()
        elif readbox == '2':
            readbox = mailbox.sent_folder()
        elif readbox == '3':
            readbox = mailbox.junk_folder()
        else:
            readbox = mailbox.deleted_folder()
        for messages in readbox.get_messages(limit=150, batch=2000):
            print(messages)
        os.system('pause')


    def send_email(self):
        self.to_who = []
        new_people = input('\n收件人是谁？\n')
        self.to_who.append(new_people)
        self.subj = input('\n主题是什么？\n')
        self.text = input('\n 正文是什么？\n')
        m = account.new_message()
        m.to.add(self.to_who)
        m.subject = self.subj
        m.body = self.text
        m.send()
        print('\n邮件已发送\n')
        os.system('pause')

    def get_full_send_info(self):
        self.to_who = []
        new_people = input('\n收件人是谁？\n')
        self.to_who.append(new_people)
        self.subj = input('\n主题是什么？\n')
        self.text = input('\n 正文是什么？\n')