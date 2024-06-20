from selenium.webdriver import Firefox

def before_scenario(context, scenario):
# def before_scenario(context):
    context.browser = Firefox()

def after_scneario(context,scenario):
# def after_scneario(context):
    context.browser.quit()