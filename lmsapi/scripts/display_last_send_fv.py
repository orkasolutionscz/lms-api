from api_global.models import GlobalVars


def run():
    vars = GlobalVars.objects.filter(varname='last_fv_send_id')
    for i in vars:
        print(i.varvalue)

