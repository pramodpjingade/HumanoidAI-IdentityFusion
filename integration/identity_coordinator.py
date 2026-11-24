
from integration.face_adapter import recognize_face
from integration.voice_adapter import recognize_voice
from integration.identity_fusion import fuse_identity


def identify_person():

    print("\nChecking face identity...")
    face_name = recognize_face()
    print("Face result:", face_name)

    print("\nChecking voice identity...")
    voice_name = recognize_voice()
    print("Voice result:", voice_name)

    result = fuse_identity(face_name, voice_name)

    print("\n========== IDENTITY FUSION ==========")
    print("Status:", result["status"])
    print("Identity:", result["identity"])
    print("Sources:", result["sources"])

    if result["status"] == "MISMATCH":
        print("WARNING: Face and voice identify different people!")

    return result


if __name__ == "__main__":
    identify_person()
