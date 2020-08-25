from webview import create_window,start
create_window(title='上海建工',url='https://www.scg.com.cn/',width=1000,height=800,resizable=True,text_select=True,confirm_close=True)
start(localization={'global.quitConfirmation':'确定关闭窗口吗？'})