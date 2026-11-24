from integration.identity_fusion import fuse_identity


test_cases = [
    ("PRAMOD P JINGADE", "PRAMOD P JINGADE"),
    ("SIDDU", None),
    (None, "PRAMOD P JINGADE"),
    ("SIDDU", "PRAMOD P JINGADE"),
    (None, None)
]

for face, voice in test_cases:
    result = fuse_identity(face, voice)

    print("\nFace:", face)
    print("Voice:", voice)
    print("Fusion:", result)