from enum import IntEnum, unique


@unique
class Types(IntEnum):
    TEXT = 1
    DOCUMENT = 2
    PHOTO = 3
    VIDEO = 4
    STICKER = 5
    AUDIO = 6
    VOICE = 7
    VIDEO_NOTE = 8
    ANIMATION = 9
    ANIMATED_STICKER = 10
    CONTACT = 11


def get_message_type(msg):
    if msg.text or msg.caption:
        content = None
        message_type = Types.TEXT
    elif msg.sticker:
        content = msg.sticker.file_id
        message_type = Types.STICKER

    elif msg.document:
        if msg.document.mime_type == "application/x-bad-tgsticker":
            message_type = Types.ANIMATED_STICKER
        else:
            message_type = Types.DOCUMENT
        content = msg.document.file_id

    elif msg.photo:
        content = msg.photo.file_id  # last elem = best quality
        message_type = Types.PHOTO

    elif msg.audio:
        content = msg.audio.file_id
        message_type = Types.AUDIO

    elif msg.voice:
        content = msg.voice.file_id
        message_type = Types.VOICE

    elif msg.video:
        content = msg.video.file_id
        message_type = Types.VIDEO

    elif msg.video_note:
        content = msg.video_note.file_id
        message_type = Types.VIDEO_NOTE

    elif msg.animation:
        content = msg.animation.file_id
        message_type = Types.ANIMATION

    # TODO
    # elif msg.contact:
    # 	content = msg.contact.phone_number
    # 	# text = None
    # 	message_type = Types.CONTACT

    # TODO
    # elif msg.animated_sticker:
    # 	content = msg.animation.file_id
    # 	text = None
    # 	message_type = Types.ANIMATED_STICKER

    else:
        return None, None

    return content, message_type


def get_note_type(msg):
    if len(msg.text.split()) <= 1:
        return None, None, None, None
    data_type = None
    content = None
    raw_text = msg.text.markdown if msg.text else msg.caption.markdown
    args = raw_text.split(None, 2)
    # use python's maxsplit to separate cmd and args
    note_name = args[1]
    reply = msg.reply_to_message
    # determine what the contents of the filter are - text, image, sticker, etc
    if len(args) >= 3:
        text = args[2]
        data_type = Types.TEXT

    elif reply:
        if reply.text:
            text = reply.text.markdown
        elif reply.caption:
            text = reply.caption.markdown
        else:
            text = ""
        if len(args) >= 2 and reply.text:  # not caption, text
            data_type = Types.TEXT

        elif reply.sticker:
            content = reply.sticker.file_id
            data_type = Types.STICKER

        elif reply.document:
            if reply.document.mime_type == "application/x-bad-tgsticker":
                data_type = Types.ANIMATED_STICKER
            else:
                data_type = Types.DOCUMENT
            content = reply.document.file_id

        elif reply.photo:
            content = reply.photo.file_id  # last elem = best quality
            data_type = Types.PHOTO

        elif reply.audio:
            content = reply.audio.file_id
            data_type = Types.AUDIO

        elif reply.voice:
            content = reply.voice.file_id
            data_type = Types.VOICE

        elif reply.video:
            content = reply.video.file_id
            data_type = Types.VIDEO

        elif reply.video_note:
            content = reply.video_note.file_id
            data_type = Types.VIDEO_NOTE

        elif reply.animation:
            content = reply.animation.file_id
            # text = None
            data_type = Types.ANIMATION

    # TODO
    # elif reply.contact:
    # 	content = reply.contact.phone_number
    # 	# text = None
    # 	data_type = Types.CONTACT

    # TODO
    # elif reply.animated_sticker:
    # 	content = reply.animation.file_id
    # 	text = None
    # 	data_type = Types.ANIMATED_STICKER

    else:
        return None, None, None, None

    return note_name, text, data_type, content


def get_welcome_type(msg):
    data_type = None
    content = None
    reply = msg.reply_to_message
    if reply:
        if reply.text:
            text = reply.text.markdown
        elif reply.caption:
            text = reply.caption.markdown
        else:
            text = None
    else:
        text = msg.text.split(None, 1)

    if reply:
        if reply.text:
            text = reply.text.markdown
            data_type = Types.TEXT

        elif reply.sticker:
            if reply.document.mime_type == "application/x-tgsticker":
                data_type = Types.ANIMATED_STICKER
            else:
                data_type = Types.STICKER
            content = reply.sticker.file_id
            text = None

        elif reply.document:
            if reply.document.mime_type == "application/x-bad-tgsticker":
                data_type = Types.ANIMATED_STICKER
            else:
                data_type = Types.DOCUMENT
            content = reply.document.file_id
        # text = reply.caption

        elif reply.photo:
            content = reply.photo[-1].file_id  # last elem = best quality
            # text = reply.caption
            data_type = Types.PHOTO

        elif reply.audio:
            content = reply.audio.file_id
            # text = reply.caption
            data_type = Types.AUDIO

        elif reply.voice:
            content = reply.voice.file_id
            text = None
            data_type = Types.VOICE

        elif reply.video:
            content = reply.video.file_id
            # text = reply.caption
            data_type = Types.VIDEO

        elif reply.video_note:
            content = reply.video_note.file_id
            text = None
            data_type = Types.VIDEO_NOTE

        elif reply.animation:
            content = reply.animation.file_id
            # text = None
            data_type = Types.ANIMATION

    # TODO
    # elif reply.animated_sticker:
    # 	content = reply.animation.file_id
    # 	text = None
    # 	data_type = Types.ANIMATED_STICKER

    else:
        if msg.caption:
            text = msg.caption.split(None, 1)
            if len(text) >= 2:
                text = msg.caption.markdown.split(None, 1)[1]
        elif msg.text:
            text = msg.text.split(None, 1)
            if len(text) >= 2:
                text = msg.text.markdown.split(None, 1)[1]
        data_type = Types.TEXT

    return text, data_type, content
