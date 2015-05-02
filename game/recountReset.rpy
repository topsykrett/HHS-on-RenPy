init python:
    def dailyRecount(chars):
        for x in chars:
            x.setCorr((getPar(teachers, 'corr') - x.corr)/10)
            x.rep += ((getPar(studs, 'rep') - x.rep)/100)