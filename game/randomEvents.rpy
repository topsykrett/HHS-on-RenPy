label event_loc_home_15_1:
    $ dynpicto = studs[0].picto
    studs[0].say "поймал1!"
    'пусто'
    $ move(curloc)

    
label event_loc_dreams_10_1:
    show expression ("pic/locations/home/dream/1.jpg") at top
    'На этот раз сон был о том, как Вы купаетесь в деньгах с бывшей одноклассницей. Во сне Вы немного перебрали шампанского, и теперь без зазрения совести позволяете себя лапать этому странному существу.'
    'Даже во сне Вы умудрились смутиться, и, проснувшись, обнаружили приятную теплоту в трусиках.'
    $ player.lust += 10
    $ move(curloc)

label event_loc_dreams_0_2:
    show expression ("pic/locations/home/dream/2.jpg") at top
    'Ужасный сон о красношапных, мальчиках терроризирующих пикачу, не дал Вам нормально выспаться.'
    $ player.energy -= 100
    $ move(curloc)
    
label event_loc_dreams_0_3:
    show expression ("pic/locations/home/dream/3.jpg") at top
    'Вам приснилась странная гравюра с японской женщиной под яблоней. Она навеяла Вам воспоминания о матери.'
    'Развратные мысли немного развеялись и Вы отлично выспались'
    $ player.energy += 100
    $ player.lust -= 10
    $ move(curloc)
    
label event_loc_dreams_5_4:
    show expression ("pic/locations/home/dream/4.jpg") at top
    'Вам приснился бывший бойфренд. Ну не то, чтобы именно он, но Вы искренне надеетесь на это.'
    'Не хотелось бы думать, что эти тропические температуры в паху вызваны незнакомцем. Ооох....'
    'Ваше желание увеличилось'
    $ player.lust += 10
    $ move(curloc)

label event_loc_dreams_0_5:
    show expression ("pic/locations/home/dream/5.jpg") at top
    'Замечательный сон о барбекю на пляже настроил Вас на благодушный лад с утра. Только перекусить захотелось...'
    $ move(curloc)
    
label event_loc_dreams_20_6:
    show expression ("pic/locations/home/dream/6.jpg") at top
    'Вам приснилась стоящая у замёрзшего пруда странная девочка с кожанными крылышками. Маленькие ледяные олени у озера вызвали у Вас только симпатию.'
    'Странный сон, оказывается суккубы способны вызывать не только желание'
    'Ваше желание немного уменьшилось'
    $ player.lust -= 10
    $ move(curloc)
    
label event_loc_dreams_25_7:
    show expression ("pic/locations/home/dream/7.jpg") at top
    'Это был ужасно беспокойный и вместе с тем развратный сон. Всю жизнь Вы прожили как демонолог. Причём МУЖСКОГО пола. В последнюю ночь Вы решили себя побаловать маленькой суккубой!'
    'Боже, как она ласково облизывала Ваш 20 сантиметровый член!'
    'Проснувшись Вы с удивлением понимаете, что даже жалеете о том, что Вам никогда не испытать удовольствия от пламенного язычка на головке. При воспоминании об этом соитии, у Вас начинает течь по ножкам'
    'Ваше желание максимально'
    $ player.lust = 100
    $ move(curloc)
    
label event_loc_dreams_40_8:
    show expression ("pic/locations/home/dream/8.jpg") at top
    'Это был пикантный и волшебный сон. В нём Вы оказались маленькой колдуньей <<rand(100,200)>> лет от роду. За столь долгий период жизни, Вы настолько пресытились ласками женщин и удовольствиями от мужчин, что решили наградить одну из своих любимых рабынь членом.'
    'Не в силах совладать с новыми ощущениями от одновременного вида огромной плоти и грудей, Вы занимались любовью где это только было возможно. На ковре у камина, прижимаясь спиной к прохладной стенке темницы, даже сидя за роялем - не могли удержать бешенного желания!'
    'Как же было прекрасно скользить своими маленькими булочками по огромному уду рабыни. Как нежно трепетали стенки влагалища, когда в него вторгалась набухшая головка члена!'
    'Вы даже ничуть не расстроились, что Вас разбудил не будильник, а конвульсии оргазма.'
    'Утренний оргазм уменьшил желание, но увеличил развращённость'
    $ player.lust -= 50
    $ player.setCorr(1)
    $ move(curloc)
    
label event_loc_dreams_15_9:
    show expression ("pic/locations/home/dream/9.jpg") at top
    'Вам приснилось, что Вас застукали ученики, когда Вы возвращались утром с рейверской вечеринки. Непонятно почему, но стыдно до сих пор.'
    'Развратность уменьшилась.'
    $ player.decCorr(1)
    $ move(curloc)
    
label event_loc_dreams_0_10:
    show expression ("pic/locations/home/dream/10.jpg") at top
    'Вам снится, что Вас уволили, и Ваши ученики с радостью выпроваживают Вас за ворота школы. Ужасно, просто ужасно. Вы проснулись в холодном поту.'
    $ move(curloc)
    
label event_loc_dreams_25_11:
    show expression ("pic/locations/home/dream/11.jpg") at top
    'В этом сне Вы были королевой. Вызванные Вами специально отобранные рабы получили совершенно неоднозначный приказ к исполнению.'
    'И вот, Ваши великолепные ножки, привыкшие к ежедневным лошадиным скачкам, задраны вверх и мощная плоть раба вторгается в королевское лоно, раздвигая нежные складки, полностью заполняя собой высокородную промежность.'
    'Остальные два раба ждали своей очереди, по опыту зная, что одним колом Ваше Королевское Величество не насытится. И бесконечные оргазмы во сне были прерваны одним, но наяву.'
    'Утренний оргазм уменьшил желание, но увеличил развращённость.'
    $ player.lust -= 30
    $ player.setCorr(1)
    $ move(curloc)
    
label event_loc_dreams_50_12:
    show expression ("pic/locations/home/dream/12.jpg") at top
    'Вам снится сон, в котором Вы нашли огромный, перевитый венами, мужской половой орган. Он возвышался над Вами, такой живой, с бархатистой кожей, блестящей головкой и она, Вы знали, жаждалa прикосновений.'
    'Не выдержав, Вы как смогли приласкали его, гладя ладонями, всем телом, обвиваясь вокруг этого столба. И Вашей наградой был поток пряно-пахнувшей белой жидкости, его было много, безумно много и Вы были счастливы.'
    'Проснувшись Вы удивились странному сну, но в паху приятно покалывало.'
    $ player.lust += 20
    $ move(curloc)
    
label event_loc_dreams_60_13:
    show expression ("pic/locations/home/dream/13.jpg") at top
    'Сегодня в Вашем сне ученики младших классов устроили небольшие соревнования, о которых, Вы уверены, они не будут рассказывать родителям. Вас это ничцть не смутило, ведь чем бы дитя не тешилось.'
    'Развращенность немного повысилась.'
    $ player.setCorr(0.5)
    $ move(curloc)
    
label event_loc_dreams_40_14:
    show expression ("pic/locations/home/dream/14.jpg") at top
    'В этом сне в женском туалете Вашей школы собрались девушки, с.. кхм... довольно большими отклонениями. Особых запах заполнял все пространство, они Вас явно не ждали, но даже, как Вам показалось, обрадовались.'
    'Проснувшись, Вы вздохнули, думая о сочетании упругих грудок и великолепного члена.'
    $ player.lust += 10
    $ move(curloc)
    
label event_loc_dreams_25_15:
    show expression ("pic/locations/home/dream/15.jpg") at top
    'Вам снится компьютерная игра. Да это так: есть шкала жизней, особых ударов, имя персонажа, но вот только удары тут наносятся вполне определенные, и судя по всему, кто первый ощутит взрыв оргазма - тот и победил.'
    'Проснувшись, Вы выкинули увиденное из головы. Игры играми, но жизнь гораздо интереснее.'
    $ player.lust += 10
    $ move(curloc)
    
label event_loc_dreams_10_16:
    show expression ("pic/locations/home/dream/16.jpg") at top
    'Вам сниться свадьба. Парадно одетый жених, одобрительно посматривает на свою половинку в довольно интересном платье, открывающим не менее интересное положение невесты. "Надеюсь у них все будет хорошо", - и с этой мыслью сон завершается.'
    'Вы отлично выспались.'
    $ player.energy += 150
    $ move(curloc)
    
label event_loc_dreams_0_17:
    show expression ("pic/locations/home/dream/17.jpg") at top
    'Вам сниться прогулка по городу в закатном свете. Чистый воздух, приятный шелест листвы, длинные тени сопровождают Вас в этой прогулке и наполняют душу покоем.'
    'Вы отлично выспались.'
    $ player.energy += 150
    $ move(curloc)
    
label event_loc_dreams_70_18:
    show expression ("pic/locations/home/dream/18.jpg") at top
    'В сегодняшнем сне, будучи дриадой, невинные заигрывания с сатиром привели к неожиданному финалу: поймав и уложив Вас на покрытую зеленое возвышение, его пальцы снизу раздвинули половые губы, и что то очень твердое и тупое уперлось в Вашу вагину.'
    'Вы сделали последнюю попытку вырваться, понимая, что проникновение ТАКОГО члена будет непростым. Бесполезно. На ощущение собственной беспомощности и бессилия, нижнее естество отреагировало предательски - влагалище намокло горячей сладостью. И сатир ПРОНИК...'
    'Вы никогда не сталкивалась с членом такой толщины. Нижние губы обхватившие член, оказались натянутыми так, что первым ощущением от проникновения была боль. Его первое движение было глубоким и медленным. Насильник явно смаковал его.'
    'Распиравший Вас член двигался все дальше и дальше вглубь, уперся в заднюю стенку матки. В первый раз показалось, что член заполнил Вас всю, Вы застонали, рогатый отпрянул своим тазом назад, высвобождая член, густо смазанный соками вожделения и снова загнал его внутрь, продолжая насиловать Вас.'
    'Ваше желание максимально.'
    $ player.lust = 100
    $ player.setCorr(1)
    $ move(curloc)
    
label event_loc_dreams_80_19:
    show expression ("pic/locations/home/dream/19.jpg") at top
    'Вам снится как шесть девушек(в числе которых и Вы) нежно ублажают парня с немалым достоинством. В конечном итоге ласки прекрасных див приводят к настоящему взрыву страсти, мощным потоком оросив всех !!!'
    'Проснувшись Вы почувствовали как теплая, щемящая и сладострастная волна, зародившись между ног, распространяется по всему телу. Утренний оргазм уменьшил желание, но увеличил развращённость.'
    $ player.lust -= 50
    $ player.setCorr(0.5)
    $ move(curloc)
    
label event_loc_dreams_0_19:
    if player.corr < 20:
        show expression ("pic/locations/home/dream/200.jpg") at top
        'В этом сне Вы смиренно просили Господа избавить Вас от соблазнов, одолевающих Вас каждую минуту, просили отвратить от Вас искушение, не вводить во грех. Вы проклинали Ваше тело, которое столько чувствительно, столь притягательно, Ваши округлые бедра, холмики больших грудей с выпирающими сосками. Ведь Вам так трудно удержаться от собственных ласк. Молитва продолжалась долго..'
    elif player.corr < 80:
        show expression ("pic/locations/home/dream/201.jpg") at top
        'Вам снилось как Вы, будучи монахиней, не смогли справиться с демоном искушения, одолевающим Ваше великолепное тело. Не выдержав, Вы подняли подол своего платья и запустив длинные пальчики под белье вложили пальчики в полыхающее страстью отверстие. Полные груди с выпирающими под платьем сосками тяжело поднимались, бедра,  слегка  отстраненные  в предвкушении,  извивались, Ваши губы вздрагивали, обнажая ряд белоснежных  зубов.'
        'Ваше желание и развращенность увеличились'
        $ player.lust += 10
        $ player.setCorr(0.5)
    else :
        show expression ("pic/locations/home/dream/202.jpg") at top
        'Вам снилось как Вы, будучи монахиней, потерпели сокрушительное поражения от демона соблазнов и, не избегнув искушения ласкали себя прямо в храме. Ваши глаза полуоткрыты, одной рукой Вы быстро освободили грудь от одежды, а второй,  чуть раздвинув ножки, неистово ласкали свою истекающую соками промежность. Перед глазами вставали сладострастные картины, и миг блаженства приближался с неумолимостью Апокалипсиса.'
        'Утренний оргазм уменьшил желание, но увеличил развращённость.'
        $ player.lust -= 50
        $ player.setCorr(0.5)
    $ move(curloc)
    
label event_loc_dreams_40_21:
    show expression ("pic/locations/home/dream/21.jpg") at top
    'В жарком Египте невольники с огромными членами неутомимо трудились над Вашим царственным телом. Отдавая свое роскошное, смазанное маслом тело, Вы с наслаждением насаживали себя на член раба до самого конца, чувствуя, как промежность приятно растянулась в самом толстом месте у основания его члена.'
    'Вы сами выбирали ритм, сами выбирали углы проникновения, импровизировали и торжествовали над ними.'
    'Проснувшись Вы почувствовали как теплая, щемящая и сладострастная волна, зародившись между ног, распространяется по всему телу. Утренний оргазм уменьшил желание, но увеличил развращённость'
    $ player.lust -= 50
    $ player.setCorr(0.5)
    $ move(curloc)
    
label event_loc_dreams_50_22:
    show expression ("pic/locations/home/dream/22.jpg") at top
    'В этом сне Вы, элитная куртизанка, вызвались удовлетворять богатых купцов из Африки. За долгие дни в море они соскучились по женскому теплу и Вы чувствуете их напряженное желание. Оседлав одного купца с его великолепным черным членом, Вы почувствовали, как его жадные руки вцепились в Вашу роскошную грудь.'
    'В алые губы устремился второй напряженный член с распухшей, как гриб, головкой, а нетерпеливые руки последнего купца развели половинки Вашей упругой задницы, дабы занять свое место в третьем отверстии Вашего атласного тела.'
    'Вы проснулись от адского пламени в промежности'
    $ player.lust = 100
    $ move(curloc)
    
label event_loc_dreams_80_23:
    show expression ("pic/locations/home/dream/23.jpg") at top
    'На этот раз сон был о том, как Вы, будучи дворянкой, всесильной в своих владениях, жили в своем поместье, развлекаясь как только могли.'
    'И вот однажды, в Вашу голову пришла мысль о том, чтобы принять ванну из мужского семени, ведь это так освежает и питает кожу (по мнению британских ученых)'
    'Собрав холопов, Вы улеглись в ванную и отдали приказ "НАПОЛНИТЬ!!!". Сотня мужиков поочередно изливались в емкость, наполняя ее терпким семенем.'
    'Ровные строи ложились на лицо, покрывали потоками большую грудь, ложились на ноги и лицо, проникали внутрь влагалища. Были ли Вы счастливы? Вполне возможно :)'
    'Развращенность повысилась'
    $ player.setCorr(1)
    $ move(curloc)
    
label event_loc_dreams_10_24:
    show expression ("pic/locations/home/dream/24.jpg") at top
    'В этом сне к Вам пришло воспоминание из детства, когда маленький братишка боялся спать один и приходил к Вам. Он уютно устраивался на Вашей груди, и со счастливой улыбкой засыпал. Это было так мило...'
    'Воспоминание было очень приятным и Вы отлично выспались'
    $ player.energy += 150
    $ move(curloc)