import traceback, json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from datetime import date
from datetime import timedelta


@Client.on_message(filters.command("plan2", [".", "/"]))
async def cmd_plan2(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @nairobiangoon !</b>"""
            await message.reply_text(resp, message.id)
            return

        user_id            = message.text.split(" ")[1]
        paymnt_method      = "CRYPTO"
        registration_check = await getuserinfo(user_id)
        registration_check = str(registration_check)
        if registration_check == "None":
            resp = f"""<b>
Silver Plan Activation Failed ❌
━━━━━━━━━━━━━━
User ID : <a href="tg://user?id={user_id}"> {user_id}</a> 
Plan Name: Silver Plan For 15 Days 
Reason : Unregistered Users

Status : Failed
</b>"""
            await message.reply_text(resp, message.id)
            return

        await check_negetive_credits(user_id)
        await getplan2(user_id)
        receipt_id  = await randgen(len=10)
        gettoday    = str(date.today()).split("-")
        yy          = gettoday[0]
        mm          = gettoday[1]
        dd          = gettoday[2]
        today       = f"{dd}-{mm}-{yy}"
        getvalidity = str(date.today() + timedelta(days=15)).split("-")
        yy          = getvalidity[0]
        mm          = getvalidity[1]
        dd          = getvalidity[2]
        validity    = f"{dd}-{mm}-{yy}"

        user_resp = f"""<b>
Thanks For Purchasing Our Silver Plan ✅

ID : <code>{user_id}</code>
Plan : Silver
Price : 15$
Purchase Date: {today}
Expiry : {validity}
Validity: 15 Days
Status : Paid ☑️
Payment Method : {paymnt_method}.
Receipt ID : MASTER-{receipt_id}

This is a receipt for your plan.saved it in a Secure Place.This will help you if anything goes wrong with your plan purchases .

Have a Good Day .
- @checkskebot
</b>"""
        try:
            await Client.send_message(user_id, user_resp)
        except:
            pass

        ad_resp = f"""<b>
Silver Plan Activated ✅ 
━━━━━━━━━━━━━━
User ID : <a href="tg://user?id={user_id}"> {user_id}</a> 
Plan Name: Silver Plan For 15 Days 
Plan Expiry: {validity} 

Status : Successfull
        </b>"""
        await message.reply_text(ad_resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
