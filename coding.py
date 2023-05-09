import os
from flask import *

from werkzeug.utils import secure_filename

from src.dbconnection import *
app=Flask(__name__)
app.secret_key="1234"



import functools

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('LOGIN_REGISTRATION/loginindex.html')
        return func()
    return secure_function

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/')
def main():
    return render_template('LOGIN_REGISTRATION/loginindex.html')

@app.route('/LOGIN',methods=['post'])
def LOGIN():
    uname=request.form['textfield']
    password=request.form['textfield3']
    qry="SELECT * FROM `login` WHERE `username`=%s AND `password`=%s "
    val=(uname,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location="/"</script>'''
    elif res['type']=='admin':
        session['lid'] = res['id']

        return '''<script>alert("welcome");window.location="/ad_home"</script>'''
    elif res['type']=='expert':
        session['lid']=res['id']
        return '''<script>alert("welcome");window.location="/ex_home"</script>'''
    elif res['type'] == 'trainer':
        session['lid'] = res['id']
        return '''<script>alert("welcome");window.location="/tr_home"</script>'''
    elif res['type'] == 'user':
        session['lid'] = res['id']
        return '''<script>alert("welcome");window.location="/ur_home"</script>'''
    else:
        return '''<script>alert("invalid");window.location="/"</script>'''

@app.route('/trainer_reg',methods=['post'])
def trainer_reg():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    phno=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    email=request.form['textfield7']
    experience=request.form['textfield8']
    usrname=request.form['textfield9']
    pwd=request.form['textfield10']
    qr = "select * from login where username=%s"
    res = selectone(qr, usrname)
    print(res)
    if res is None:
        qry="insert into login values(null,%s,%s,'pending')"
        val=(usrname,pwd)
        lid=iud(qry,val)
        qry2="insert into `trainer_register` values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val2=(str(lid),fname,lname,phno,place,post,pin,email,experience)
        iud(qry2,val2)
        return '''<script>alert("success");window.location="/"</script>'''
    else:
        return '''<script>alert("Username exist");window.location="/"</script>'''

@app.route('/user_reg',methods=['post'])
def user_reg():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    email=request.form['textfield3']
    phno=request.form['textfield4']
    place=request.form['textfield5']
    post=request.form['textfield6']
    pin=request.form['textfield7']
    usrname=request.form['textfield8']
    pwd=request.form['textfield9']
    qr="select * from login where username=%s"
    res=selectone(qr,usrname)
    print(res)
    if res is  None:
        qry = "insert into login values(null,%s,%s,'user')"
        val = (usrname, pwd)
        lid = iud(qry, val)
        qry2 = "insert into `user_register` values(null,%s,%s,%s,%s,%s,%s,%s,%s)"
        val2 = (str(lid), fname, lname, email, phno, place, post, pin)
        iud(qry2, val2)
        return '''<script>alert("success");window.location="/"</script>'''
    else:
        return '''<script>alert("Username exist");window.location="/"</script>'''

@app.route('/expert_reg',methods=['post'])
@login_required
def expert_reg():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    phno=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    email=request.form['textfield7']
    usrname=request.form['textfield8']
    pwd=request.form['textfield9']

    qry="insert into login values(null,%s,%s,'expert')"
    val=(usrname,pwd)
    lid=iud(qry,val)
    qry2="insert into `expert` values(null,%s,%s,%s,%s,%s,%s,%s,%s)"
    val2=(str(lid),fname,lname,phno,place,post,pin,email)
    iud(qry2,val2)
    return '''<script>alert("success");window.location="/ad_mngexp"</script>'''

@app.route('/LOGOUT')
def LOGOUT():
    return render_template('LOGIN_REGISTRATION/LOGIN.html')

#-----------------------------------------
@app.route('/t_reg')
def reg():
    return render_template('LOGIN_REGISTRATION/trainerregindex.html')

@app.route('/u_reg')
def regu():
    return render_template('LOGIN_REGISTRATION/userregindex.html')

@app.route('/ad_home')
@login_required
def ad_insti():
    return render_template('ADMIN_MODULE/adminindex.html')

@app.route('/ad_vf')
@login_required
def ad_vf():
    qry="select * from feedback join user_register on feedback.user_id=user_register.login_id"
    res=selectall(qry)
    return render_template('ADMIN_MODULE/VIEW_FEEDBACK.html',val=res)

@app.route('/ad_expert')
@login_required
def ad_expert():
    return render_template('ADMIN_MODULE/ADD EXPERT.html')

@app.route('/ad_blunbl')
@login_required
def ad_blunbl():
    qry="select user_register.*,login.* from user_register join login on user_register.login_id=login.id"
    res=selectall(qry)
    return render_template('ADMIN_MODULE/BLOCK &UNBLOCK.html',val=res)

@app.route('/ad_mngexp')
@login_required
def ad_mngexp():
    qry="select * from expert"
    res=selectall(qry)
    return render_template('ADMIN_MODULE/MNGEXPERT.html',val=res)


@app.route('/EDIT_EXPERT')
@login_required
def EDIT_EXPERT():
    id=request.args.get('id')
    session['eid']=id
    qry="select * from expert where id=%s"
    res=selectone(qry,id)
    return render_template('ADMIN_MODULE/EDIT_EXPERT.html',val=res)



@app.route('/ad_expert_update',methods=['post'])
@login_required
def ad_expert_update():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    phno = request.form['textfield3']
    place = request.form['textfield4']
    post = request.form['textfield5']
    pin = request.form['textfield6']
    email = request.form['textfield7']

    qry="update expert set first_name=%s,last_name=%s,phno=%s,place=%s,post=%s,pin=%s,email_id=%s where id=%s"
    val=(fname,lname,phno,place,post,pin,email,session['eid'])
    iud(qry,val)
    return '''<script>alert("success");window.location="/ad_mngexp"</script>'''



@app.route('/ad_delete_exp')
@login_required
def ad_delete_exp():
    id=request.args.get('id')
    qry="delete  from expert where login_id=%s"
    iud(qry,id)
    qr="delete from login where id=%s"
    iud(qr,id)
    return '''<script>alert("deleted");window.location="/ad_mngexp"</script>'''



@app.route('/ad_block')
@login_required
def ad_block():
    id = request.args.get('id')
    qry = "update login set type='pending' where id=%s"
    iud(qry, id)
    return '''<script>alert("BLOCKED");window.location="/ad_blunbl"</script>'''



@app.route('/ad_unblock')
@login_required
def ad_unblock():
    id = request.args.get('id')
    qry = "update login set type='user' where id=%s"
    iud(qry, id)
    return '''<script>alert("UNBLOCKED");window.location="/ad_blunbl"</script>'''





#-----------------------------------------


@app.route('/ex_home')
@login_required
def ex_home():
    return render_template('EXPERT_MODULE/expertindex.html')

@app.route('/ex_vat')
@login_required
def ex_vat():
    qry="SELECT trainer_register.*,login.type FROM login  JOIN trainer_register ON login.id=trainer_register.log_id"
    res=selectall(qry)
    return render_template('EXPERT_MODULE/VERIFY & ASSIGN TRAINERS.html',val=res)

@app.route('/ex_aswrk')
@login_required
def ex_aswrk():
    id=request.args.get('id')
    session['trid']=id
    qry = "select * from user_register"
    res = selectall(qry)
    return render_template('EXPERT_MODULE/ASSIGN WORK.html',val=res)

@app.route('/ex_aswrk_add',methods=['post'])
@login_required
def ex_aswrk_add():
    user=request.form['select']
    time=request.form['textfield']
    date=request.form['textfield2']
    qry="insert into work values(null,%s,%s,'pending',%s,%s)"
    val = (user,session['trid'],time,date )
    iud(qry, val)
    return '''<script>alert("SUBMITTED");window.location="/ex_aswrk"</script>'''


@app.route('/ex_amt')
@login_required
def ex_amt():
    qry = "SELECT user_register.first_name,user_register.last_name,`work`.* FROM user_register JOIN work ON work.user_id=user_register.login_id"
    res = selectall(qry)
    return render_template('EXPERT_MODULE/ADD & MANAGE TIME.html',val=res)



@app.route('/ex_time_get')
@login_required
def ex_time_get():
    id = request.args.get('id')
    session['tid'] = id
    qry = "select * from work where id=%s"
    res = selectone(qry,id)
    print(res)
    return render_template('EXPERT_MODULE/EDIT USER TIME.html',val=res)

@app.route('/ex_time_update',methods=['post'])
@login_required
def ex_time_update():
    time=request.form['textfield']
    date=request.form['textfield2']
    qry="update work set time=%s,date=%s where id=%s"
    val=(time,date,session['tid'])
    iud(qry,val)
    return '''<script>alert("UPDATED");window.location="/ex_amt"</script>'''


@app.route('/ex_time_delete')
@login_required
def ex_time_delete():
    id=request.args.get('id')
    qry="delete from work where id=%s"
    iud(qry,id)
    return '''<script>alert("deleted");window.location="/ex_amt"</script>'''

@app.route('/ex_ut')
@login_required
def ex_ut():
    qry="select * from user_register"
    res=selectall(qry)
    return render_template('EXPERT_MODULE/USER TIME.html',val=res)

@app.route('/ex_ut_add',methods=['post'])
@login_required
def ex_ut_add():
    name= request.form['select']
    time= request.form['textfield']
    date= request.form['textfield2']
    qry="insert into time_register values(null,%s,%s,%s)"
    val = (name,time,date)
    iud(qry, val)
    return '''<script>alert("success");window.location="/ex_ut"</script>'''





@app.route('/ex_amv')
@login_required
def ex_amv():
    qry="select * from videos"
    res=selectall(qry)
    return render_template('EXPERT_MODULE/ADD & MANAGE VIDEOS.html',val=res)

@app.route('/ex_av')
@login_required
def ex_av():
    return render_template('EXPERT_MODULE/ADD VIDEO.html')

@app.route('/ex_av_add',methods=['post'])
@login_required
def ex_av_add():
    video=request.files['file']
    fn=secure_filename(video.filename)
    video.save(os.path.join('static/videos',fn))
    qry="insert into videos values(null,%s,%s,curdate())"
    val=(session['lid'],fn)
    iud(qry,val)
    return '''<script>alert("success");window.location="/ex_amv"</script>'''




@app.route('/ex_vu')
@login_required
def ex_vu():
    qry="SELECT first_name,last_name,phno,mail_id,place,post,pin FROM user_register"
    res=selectall(qry)
    return render_template('EXPERT_MODULE/VIEW USER.html',val=res)




@app.route('/ex_av_delete')
@login_required
def ex_av_delete():
    vid=request.args.get('did')
    qry="delete from videos where id=%s"
    iud(qry,vid)
    return '''<script>alert("deleted");window.location="/ex_amv"</script>'''


@app.route('/ex_accept')
@login_required
def ex_accept():
    id=request.args.get('id')
    qry="update login set type='trainer' where id=%s"
    iud(qry,id)
    return '''<script>alert("DONE");window.location="/ex_vat"</script>'''

@app.route('/ex_reject')
@login_required
def ex_reject():
    id=request.args.get('id')
    qry="update login set type='rejected' where id=%s"
    iud(qry,id)
    return '''<script>alert("REJECTED");window.location="/ex_vat"</script>'''



@app.route('/ex_ws')
@login_required
def ex_ws():
    qry="select * from work join trainer_register on trainer_register.log_id=work.trainer_id"
    res=selectall(qry)
    return render_template('EXPERT_MODULE/WORK_STATUS.html',val=res)


@app.route('/ex_ws_view')
@login_required
def ex_ws_view():
    return render_template('EXPERT_MODULE/WORK_STATUS.html')

#---------------------------------------------

@app.route('/tr_home')
@login_required
def tr_home():
    return render_template('TRAINER_MODULE/trainerindex.html')

@app.route('/tr_awu')
@login_required
def tr_awu():
    qry="select * from work join user_register on user_register.login_id=work.user_id where trainer_id=%s"
    res=selectall2(qry,session['lid'])
    return render_template('TRAINER_MODULE/ASSIGNED WORK & UPDATE.html',val=res)

@app.route('/tr_up')
@login_required
def tr_up():
    id=request.args.get('id')
    session['upid']=id
    return render_template('TRAINER_MODULE/UPDATE & STATUS.html')




@app.route('/tr_up_submit',methods=['post'])
@login_required
def tr_up_submit():
    status=request.form['select']
    qry="update work set status=%s where id=%s"
    val=(status,session['upid'])
    iud(qry,val)
    return '''<script>alert("UPDATED");window.location="/tr_awu"</script>'''





@app.route('/tr_vdr')
@login_required
def tr_vdr():
    qry="select * from  doubt join user_register on user_register.login_id=doubt.user_id"
    res=selectall(qry)
    return render_template('TRAINER_MODULE/VIEW DOUBTS AND REPLY.html',val=res)

@app.route('/tr_rpl')
@login_required
def tr_rpl():
    id=request.args.get('id')
    session['ddid']=id
    return render_template('TRAINER_MODULE/REPLY.html')



@app.route('/tr_rpl_send',methods=['post'])
@login_required
def tr_rpl_send():
    reply=request.form['textarea']
    qry="update doubt set reply=%s where id=%s"
    val = (reply,session['ddid'])
    iud(qry, val)
    return '''<script>alert("UPDATED");window.location="/tr_vdr"</script>'''

#------------------------------------------

@app.route('/ur_home')
@login_required
def ur_home():
    return render_template('USER_MODULE/userindex.html')

@app.route('/ur_askdou')
@login_required
def ur_askdou():
    return render_template('USER_MODULE/ASK DOUBTS & REPLY.html')

@app.route('/ur_doubts')
@login_required
def ur_doubts():
    qry="select * from trainer_register"
    res=selectall(qry)
    return render_template('USER_MODULE/ASK DOUBTS.html',val=res)

@app.route('/ur_doubts_send',methods=['post'])
@login_required
def ur_doubts_send():
    trainer=request.form['select']
    doubt=request.form['textfield']
    qry="insert into doubt values(null,%s,curdate(),%s,'pending',%s)"
    val =( session['lid'],doubt,trainer)
    iud(qry, val)
    return '''<script>alert("success");window.location="/ur_doubts"</script>'''




@app.route('/ur_feed')
@login_required
def ur_feed():
    return render_template('USER_MODULE/FEEDBACK.html')

@app.route('/ur_feed_add',methods=['post'])
@login_required
def ur_feed_add():
    feed = request.form['textfield']
    qry="insert into feedback values(null,%s,%s,curdate())"
    val = (session['lid'],feed)
    iud(qry, val)
    return '''<script>alert("success");window.location="/ur_feed"</script>'''



@app.route('/ur_seerpl')
@login_required
def ur_seerpl():
    qry="select * from doubt join trainer_register on trainer_register.log_id=doubt.trainer_id"
    res=selectall(qry)
    return render_template('USER_MODULE/SEE REPLY.html',val=res)

@app.route('/ur_time')
@login_required
def ur_time():
    qry="select * from work join trainer_register on trainer_register.log_id=work.trainer_id where work.user_id=%s"
    res=selectall2(qry,session['lid'])
    return render_template('USER_MODULE/TIME.html',val=res)

@app.route('/ur_view')
@login_required
def ur_view():
    qry="select * from videos join expert on videos.expert_id=expert.login_id"
    res=selectall(qry)
    print (res)
    return render_template('USER_MODULE/VIEW_VIDEO.html',val=res)



#---------------------------------------



app.run(debug='true')