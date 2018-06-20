from telethon import TelegramClient, events
import socks
import getpass
from telethon.errors import SessionPasswordNeededError
from configs import settings
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.users import GetFullUserRequest


client = TelegramClient('telethon_test', settings.api_id, settings.api_hash,
                        proxy=(socks.SOCKS5, settings.host, settings.port),
                        update_workers=1,
                        spawn_read_thread=False)
assert client.connect()
if not client.is_user_authorized():
    print(1)
    try:
        client.send_code_request(settings.phone_number)
        me = client.sign_in(settings.phone_number, settings.login_code)
    except SessionPasswordNeededError:
        client.sign_in(password=getpass.getpass())
else:
    print(2)
    client.start()


phone1_id = 514193575
phone2_id = 606287107

@client.on(events.NewMessage)
def my_event_handler(event):
    if 'hello' in event.raw_text:
        print(event.is_channel)
        print(event)
        event.reply('hi!')

# client(AddChatUserRequest(
#     chat_id=1290687161,
#     user_id=606287107,
#     fwd_limit=10  # Allow the user to see the 10 last messages
# ))
client(InviteToChannelRequest("1290687161", "606287107"))
# NewMessage.Event(
#     is_channel=True,
#     message=Message(
#         out=False,
#         reply_to_msg_id=None,
#         id=133, mentioned=False, reply_markup=None, from_id=606287107, post=False, entities=[],
#         to_id=PeerChannel(channel_id=1290687161), grouped_id=None, date=datetime.utcfromtimestamp(1529465843),
#         message='hello hh', fwd_from=None, media=None, views=None, edit_date=None, post_author=None, via_bot_id=None,
#         silent=False, media_unread=False),
#     is_group=True,
#     original_update=UpdateNewChannelMessage(
#         pts_count=1,
#         message=Message(
#             out=False, reply_to_msg_id=None, id=133, mentioned=False, reply_markup=None, from_id=606287107,
#             post=False, entities=[], to_id=PeerChannel(channel_id=1290687161), grouped_id=None, date=datetime.utcfromtimestamp(1529465843),
#             message='hello hh', fwd_from=None, media=None, views=None, edit_date=None, post_author=None,
#             via_bot_id=None, silent=False, media_unread=False),
#         pts=166),
#     pattern_match=None,
#     is_private=False)
#
#
# NewMessage.Event(
#     is_channel=True,
#     message=Message(
#         out=True,
#         reply_to_msg_id=133,
#         id=135, mentioned=False, reply_markup=None, from_id=514193575, post=False, entities=[], to_id=PeerChannel(channel_id=1290687161),
#         grouped_id=None, date=datetime.utcfromtimestamp(1529465877), message='hello sb', fwd_from=None, media=None, views=None,
#         edit_date=None, post_author=None, via_bot_id=None, silent=False,
#         media_unread=False),
#     is_group=True,
#     original_update=UpdateNewChannelMessage(
#         pts_count=1,
#         message=Message(out=True, reply_to_msg_id=133, id=135, mentioned=False,
#                         reply_markup=None, from_id=514193575, post=False,
#                         entities=[], to_id=PeerChannel(channel_id=1290687161), grouped_id=None,
#                         date=datetime.utcfromtimestamp(1529465877), message='hello sb', fwd_from=None, media=None, views=None,
#                         edit_date=None, post_author=None, via_bot_id=None, silent=False, media_unread=False),
#         pts=168),
#     pattern_match=None,
#     is_private=False)


client.idle()