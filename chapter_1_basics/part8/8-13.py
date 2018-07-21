def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('bulat', 'yusupov', location='russia',
                             field='development')
print(user_profile)
