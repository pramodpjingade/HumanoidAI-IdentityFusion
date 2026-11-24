UNKNOWN_NAMES = {
    "",
    "unknown",
    "unknown person",
    "unknown speaker",
    "none"
}


def is_known_identity(name):
    if name is None:
        return False

    return name.strip().casefold() not in UNKNOWN_NAMES


def fuse_identity(face_name=None, voice_name=None):

    face_known = is_known_identity(face_name)
    voice_known = is_known_identity(voice_name)

    if face_known and voice_known:

        if face_name.strip().casefold() == voice_name.strip().casefold():
            return {
                "status": "MATCH",
                "identity": face_name,
                "sources": ["face", "voice"]
            }

        return {
            "status": "MISMATCH",
            "identity": None,
            "sources": ["face", "voice"],
            "face_identity": face_name,
            "voice_identity": voice_name
        }

    if face_known:
        return {
            "status": "FACE_ONLY",
            "identity": face_name,
            "sources": ["face"]
        }

    if voice_known:
        return {
            "status": "VOICE_ONLY",
            "identity": voice_name,
            "sources": ["voice"]
        }

    return {
        "status": "UNKNOWN",
        "identity": None,
        "sources": []
    }