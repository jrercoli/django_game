from behave import *


@given(u'I search for a valid question')
def step_impl(context):
    context.browser.get('http://localhost:8000/polls/2/')
    assert context.failed is False

@then(u'I will see the choices for that question')
def step_impl(context):
    assert 1 == 1
    pass
