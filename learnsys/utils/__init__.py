# learnsys/utils/__init__.py

# Или если функции определены здесь напрямую
def is_student(user):
    return user.is_active and not user.is_staff

def is_instructor(user):
    return user.is_staff and not user.is_superuser