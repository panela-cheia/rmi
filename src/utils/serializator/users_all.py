def serialize_user(user):
    user_dict = {
        'id': user.id,
        'name': user.name,
        'username': user.username,
        'email': user.email,
        'barn': user.barn[0].__dict__,
        'followers': [follower.__dict__ for follower in user.followers],
        'following': [following.__dict__ for following in user.following],
        'owners_dive': [owner_dive.__dict__ for owner_dive in user.owners_dive],
        'photo': user.photo.__dict__ if user.photo else None,
        'reactions': [reaction.__dict__ for reaction in user.reactions],
        'recipes': [recipe.__dict__ for recipe in user.recipes],
        'users_dive': [user_dive.__dict__ for user_dive in user.users_dive]
    }
    return user_dict