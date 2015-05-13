from distutils.core import setup

setup(name='django-mailgun-validation',
    version='1.0.2',
    description='Django fields for validating email using the Mailgun API',
    author='Antonio Ognio',
    author_email='antonio@ognio.com',
    url='https://github.com/gnrfan/django-mailgun-validation',
    packages=[
        'mailgun_validation',
        'mailgun_validation.db',
        'mailgun_validation.db.models',
        'mailgun_validation.forms',
    ],
    package_dir={
        'mailgun': 'mailgun_validation',
    },
    install_requires=[
        'requests',
        'Django'
    ]
)
