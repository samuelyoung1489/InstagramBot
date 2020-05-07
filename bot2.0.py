from instapy import InstaPy
from instapy import smart_run

insta_username = ''
insta_password = ''

#Here I am setting up the library of comments that the code will choose from
comments = ['Nice shot! @{}',
        'Love this Photo! @{}',
        'So Inspiring!!',
        'Absolutely Incredible!',
        'What camera did you use?? @{}?',
        'Love your posts @{}',
        'Such a cool pic! @{}',
        'You are so inspiring! @{}',
        'Yes! This is the content I need!!',
        'So much passion in this photo @{}',
        'Incredible!']

#Here I set up the session that my code will run in
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):

#Here I set the tags that I will like based on
  session.like_by_tags(["Nature", "Hiking", "Outdoors"], amount=11)
  session.set_dont_like(["nsfw"])

#Here I set the criteria for what photos I will comment on
  session.set_do_comment(enabled=True, percentage=50)
  session.set_comments(comments)

#Here I set the criteria for who I will follow
  session.set_do_follow(True, percentage=50)


#Here I ser the criteria for who I will un-follow
  session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=601)
