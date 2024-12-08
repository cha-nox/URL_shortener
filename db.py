def create() -> None :
    try :
        from app import db
        from app.models.user import User
        from app.models.link import Link
        db.create_all()
        print("✓ Database creation SUCCESSFUL.")
    except Exception as e :
        print("✕ Database creation FAILED ! :")
        print(f"↪ {e}")
        exit(0)
    exit(1)

def drop() -> None :
    try :
        from app import db
        db.drop_all()
        print("✓ Database deletion SUCCESSFUL.")
    except Exception as e :
        print("✕ Database deletion FAILED ! :")
        print(f"↪ {e}")
        exit(0)
    exit(1)

def reset() -> None :
    try :
        from app import db
        db.drop_all()
        print("✓ Database deletion SUCCESSFUL.")
        from app.models.user import User
        from app.models.link import Link
        db.create_all()
        print("✓ Database creation SUCCESSFUL.")
    except Exception as e :
        print("✕ Database reset FAILED ! :")
        print(f"↪ {e}")
        exit(0)
    exit(1)