def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)
