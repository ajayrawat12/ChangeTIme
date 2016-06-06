from django.http import HttpResponse
import time
# Create your views here.


def changeTime(request):
    d = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six',
    '7': 'Seven', '8': 'Eight', '9': 'Nine', }

    timeCur = None

    timeCur = (time.strftime("%I:%M") + 'PM')
    t1 = list(timeCur)
    out = ''
    count = 0

    for le in t1:
        for num, word in d.iteritems():
            if num == le:
                out = out + word
                count = count + 1
                if count == 2:
                    out = out + ' ' + ':'
        continue
    out = out + ' PM'
    return HttpResponse(out)
