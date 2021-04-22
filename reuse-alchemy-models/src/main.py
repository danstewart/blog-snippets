#!/usr/bin/env python3


import models  # noqa: F401,F403
from db import db


def main():
    # Create all tables
    db.Base.metadata.create_all(bind=db.engine)

    print('> All tables in our database')
    for table in db.Base.metadata.tables.keys():
        print(table)
    print('\n')

    # Create a user
    user = models.UserProductA(
        name='Dan',
        email='dan@somewhere.co'
    )

    db.session.add(user)
    db.session.commit()

    # Add some posts
    db.session.add(models.PostProductA(
        user_id=user.id,
        body="This is a blog post",
        private=False,
    ))

    db.session.add(models.PostProductA(
        user_id=user.id,
        body="This is another blog post",
        private=True,
    ))

    # Commit the inserts
    db.session.commit()

    # List all records
    print('> All records in user_product_a')
    for user in models.UserProductA.query.all():
        print(f'<User id={user.id} name={user.name} email={user.email}>')

        # Now fetch our posts using the relationship on the model
        for post in user.posts:
            print(f'<Post id={post.id} user_id={post.id} body={post.body} private={post.private}')


if __name__ == '__main__':
    main()
