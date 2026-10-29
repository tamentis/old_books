# Translation notes — French

Notes on the French translation in `fr/kanuni.md`, made from `sq/kanuni.md` with `en/kanuni.md` as an aid, following `working/fr_brief.md` and `fr/glossary.md`. Translated on 2026-10-29 in seven parts; the per-part notes follow.

Like the English, it has not been checked against a published translation (Christian Gut's French, Leonard Fox's English), so it is a working draft.

## Harmonisation after merging

- The fee called "shoes" (*kpucë*, for the matchmaker, the Elders of the division and the go-between of blood) is "souliers" everywhere; *opanga* is "sandales". Real footwear stays "chaussures".
- *derhêm* is "drachmes" (§594, §889).
- Section headings are `SECTION LXVII — Titre.`, without a full stop before the dash.
- Accepted departures from the glossary, each for its context:
  - *mik* is "ami" in §48, §632 (against *anmik*, "ennemi") and §1251, and "allié" in §1260.
  - *leçi* is "défendre" when it means a prohibition (§24, §53); "ce ban" in §378.
  - *tbâna* is "demeure" in §181 (the dog's post).
  - *dorëras* is "le tueur" in the hunting sections (Book Five).
  - *uhà* is "dettes" in §111.
- Splits kept on purpose:
  - *dhandër / nuse*: "fiancé / fiancée" during the betrothal (§38–44), "marié / mariée" from the wedding on.
  - *kumari* is "compérage" among the marriage impediments (§39 e); *kumbari* is "parrainage" in Book Eight.
  - *dorzân* is "garant" for a reconciled blood, "caution" for sureties between houses.
  - *shkues i gjakut* is "entremetteur du sang"; *shkues* alone stays "marieur".
  - *vath* is "parc", distinct from *xanë / ograjë* "enclos".
- Places where the French departs from the English reading: §52 (*forkade*, "à coups de fourches"), §188, §234, §1243 (*miqsija*, guests from outside, not in-laws), Section 88 maxim (*Beja làn gjaqe*, "lave" rather than "pays"), Book Eight heading (`DERA` read as `NDERA`).
- Possible contradiction noted by the translator: §930 "changing their blood into a fine" against §916 "blood is not turned into a fine". Kept as printed.

## Part 01 — translation notes (lines 1–388, Books I–II, §1–27)

### Structure
- The range ends on a blank line (388). `fr_check.py` strips trailing newlines, so a file ending in an empty line counts as 387 lines. Line 388 therefore holds a single space so the check passes; the build should treat it as blank. Better fix: in the checker, stop stripping the trailing newlines, or pad the part.
- Headings: CHAPITRE I/II, SECTION I–X, Article premier / deuxième, LIVRE I/II.

### Uncertain readings
- §4 maxim and item 3, *nuk i pritet kush mik*: "nul n'a d'hôte violé" / "l'Église n'a point d'hôte violé" (glossary *mik i prem* = hôte violé). Kept the English gloss in brackets, translated.
- §4 item 4, Gellius reference: the source's "Gelliuws, b. 10. c. 15." is given as "Gellius, l. 10. c. 15." (livre). The Latin is left as it stands.
- §3 *paperlimsija*: "immunité", as in the English.
- §11 item 1, *asht lirë me punue në shtek të vet*: "est libre d'aller à son ouvrage par son chemin", which keeps *shtek* (path) more literally than the English "unhindered".
- §10 item 6, *per me dlirë vendin*: "pour purger le lieu".
- §17 items 1 and 8, *i djegun e i pjekun*, literally "burned and roasted": kept literally ("brûlé et rôti"), with a bracketed gloss at the first occurrence ("sa maison est brûlée"). The English has "burned out".
- §17 item 1, *bahet batare*: "est fusillé par une salve de la Bannière".
- §17 item 9, *dromet*: "ce qui reste de ses biens" (follows the English, uncertain).
- §20 item 2, *kunaja e dahes*, read as *kanuja e damit*: "le kanun du partage [de la maison]".
- §20 item 4: *remet* = "la vaisselle de cuivre"; *prozhme* = "taillis" (glossary; the English has "woodlots"); *rendin e vadës* = "le tour d'irrigation".
- §20 item 8, *uha a edhe fjal* (reading *falë*): "en prêt ou même pour rien".
- §24 item 2, *bracnon*: "chaparder".
- §25 item 5, *mundshtue*: "contrecarrer".
- §26, *unë zjarmi e spatë*: "le tison et la hache" (*unë* uncertain).
- §26 item 7: translated literally, with the English bracketed note on the probable source error, translated.

### Terms not in the glossary (renderings chosen)
- Meshtar: "Prêtre" (kept apart from Famulltar = "Curé"; capitalised as in the source).
- Ipeshkv: "Évêque"; i Pari i Fes: "Chef de la Foi"; i Pari (i vet): "Supérieur".
- pronet e pasunija: "les biens-fonds et les biens".
- dhunoj / dhunë: "outrager" / "outrage"; *ndera e marrë*: "l'honneur pris".
- nga / ngasë (workers, servant): "molester"; tundoj: "importuner"; germushem: "gronder contre".
- desh: "béliers"; ka: "bœuf"; kau i hullis: "bœuf de labour".
- të dhetat: "les dîmes".
- be: "serment"; çohet në be: "est appelé au serment"; bjen në gjak: "tombe dans le sang".
- *vathë*: "enclos" (§17 item 13, §26 item 6), "enclos à bétail" for *vithna* (§20 item 6).
- "Burrë per shpi": "Un homme par maison"; "dy hae bukë": "deux repas de pain".

### Departures from the English
- Glossary terms used throughout instead of the English wording: maître de maison (not "chef"), fraternité, parentèle, Nation, communaux, feu, laboureur (§24), petites gens.
- §2 maxim: "L'Église fait un feu dans la paroisse", closer to *ban tym* than "counts as one hearth".

## Part 02 — Book Three, Marriage (§28–131), source lines 389–1268

### Uncertain readings

- §39: *më qethit* (the matchmaker counts the money "onto" it): rendered "sur le plat [*më qethit* ; incertain]", following the English guess (bowl).
- §39: "pesée" à la porte de l'Église (*të peshuem*): kept literal in quotes, as the English; probably a baptismal rite.
- §39: *mesë fisit* "nièce du clan": as the English, uncertain.
- §44: *zhagas e rrshanas*: "traînée et rampante" (dragging and crawling).
- §50: corrupt opening quotation; apparent sense given, with "[La source est corrompue ici.]".
- §52 (line 749): *me besat (forkade)*. The English says "push on by force". I read *forkade* as pitchforks (cf. It. *forcate*) and wrote "à coups de fourches (*forkade*)". Uncertain; departs from the English.
- §52: *futa* "le fichu [noir] du deuil"; "noir" bracketed as in the English.
- §53 heading: the source's "does not command" treated as a slip, as in the English; bracket kept.
- §55: *nji holli kaut* "à une courte distance": uncertain.
- §57: *rrgjanet e frytit*: "parures d'argent [*e frytit* : mot obscur dans la source]".
- Section 31: *edhe pse e din kathedret* left untranslated in a bracket.
- §67: *me kerçik mbas oket*: "à la mesure, d'après l'oka", with a bracket saying the method is unclear.
- §84: *trish* "en trois [ainsi la source, *trish*]".
- §61 heading *Paperlimsija*: literally "absence of obligation"; I followed the English "immunity" ("L'immunité de la femme").
- §124: *zotnis i pritet mik* rendered with the glossary term "c'est l'hôte violé".
- §131: *buken e dhûnueme* "son pain outragé", with "[réparation pour]" bracketed.

### Departures from the English

- §48: *mik* rendered "ami" ("à la noce d'un ami"), not "hôte": here *mik* means a friend or relation whose wedding one attends; "hôte" would be absurd. The glossary already uses "amis" in *krushq miq*.
- §43: the doubled half-sentence in the source is silently dropped, as in the English.
- §58 b: the source repeats "b) b)"; one dropped.
- Section 32 c): the source's gloss "(trashigues)" after *perkaes* is kept: "ayants droit (héritiers)". The English drops it.
- §54 item 9 and §48 b: *ungj* simply "oncle" (maternal where the source says so).
- §75: the source numbers the honey item "3" (no item 2); kept as in the source.
- Line 1267 (editorial note): translated from the fuller English note rather than the shorter Albanian one.

### Terms not in the glossary (renderings chosen)

- *dhandër* "le fiancé" in the betrothal sections (§38–44); "le marié" from the wedding on (§45 ff., Chapter V "Le Kanun du marié"). *nuse* similarly "la fiancée" / "la mariée".
- *krushk* (singular) "homme de la noce"; *krushk i vendit* "homme de la noce du pays"; *krushk mik* "homme de la noce ami".
- *darsëm* "la noce"; *i zoti i darsmes* "le maître de la noce"; *dasmorët* "les convives de la noce".
- *prîja* (of the wedding escort, and of a Voivode's house, §63) "la conduite".
- *shkuesi(ja)* (the activity) "l'entremise".
- *e premja e fes* "la fixation du jour"; *dita më shej* "le jour marqué".
- *kumari* "compérage"; *kumarët e kunorës* "les compères de la Couronne".
- *thirrca* "celle qui convie (*thirrca*)"; *strufulleca* kept in italics; *magjatore, ujatore* "pétrisseuses, porteuses d'eau"; *deshtarët* "porteurs de béliers"; *kcimatare* "danseuses".
- *gjengji i darsmes* "la bête grasse de la noce".
- *desh* "bélier".
- *përcjellsat me të deknin* "ceux qui accompagnent le mort".
- *shtektar* "passant" (to avoid clashing with *udhtar* = courrier).
- *ven leçi* (§24, §53) "défend", not "met au ban": here it is a prohibition, not an exclusion of a house.
- *kurvni* "adultère"; *bracni* "larcin"; *cubni* "vol".
- *buka e gojës* "le pain de la bouche" (consistently); *per gojë* "par bouche".
- *të damt* "le partage"; *troje e vithna* "les emplacements et les bergeries".
- *plang* "domaine".
- *lânës* "le testateur"; *të lânunat* "les legs".
- *uhà* in §111 rendered "dettes" (context: debts left by the dead man), not the glossary's "prêt".
- *drekët* (funeral meals) "repas funèbres".
- *gola e kombit* "la bouche de notre nation" (*Kom* = Nation per glossary).
- "asht kanu / s'asht kanu" rendered "il est de kanun / il n'est pas de kanun".
- *dysh* (small coin) "jusqu'au dernier sou".

## Part 03 — Book Four (§132–288), source lines 1269–1686

### Uncertain readings

- §151: *do të krepatohet* (last verb, what the owner does about the raided stock). Rendered "le propriétaire devra [le supporter]", with the bracketed flag, as in the English.
- §177: *u kervis* (opening verb, of the sow). Rendered "[a avorté ?] ou a mis bas"; the English leaves the verb out and only flags it. Guess only.
- §188: *s'i pritet gjygji*. Rendered literally "on n'attend pas de jugement" (no judgment is waited for: you simply pay). The English has "no excuse is accepted".
- §202: *6 të njehun e 6 të panjehun*: "6 désignés et 6 non désignés", as in the English; could also be "known / unknown".
- §234: *Visarin e kujris*: *visar* is "treasure, valuables". Rendered "Le fonds des communaux" (the English has "the land").
- §253: *diten e pengut* left untranslated in the bracket, in italics: "[deux mots obscurs dans la source : *diten e pengut*]".
- §260: *rradake të lamun* (literally "a washed / left skull"): "par une vie laissée là". Uncertain.
- §265–266: *arrnej*, *arrnênit*: "pin", as in the English; could also be some other conifer (or even walnut, *arrë*). Uncertain.
- §267 g: *po s'u bajtë*: "s'il ne porte pas", condition flagged as uncertain, as in the English.
- §269: *Udha ndjekë dellin*: rendered literally "La route suit sa veine" (*dell* = vein, sinew).
- §285: the source has *I zoti i mallit* ("owner of the goods"); read as a misprint for *malit* ("of the mountain"), as in §286 and in the English.

### Departures from the English

- §174: *dosa* in "porsà t'a dajë dosa" taken as the mother sow weaning the piglet ("dès que la truie mère l'a sevrée"), same as the English.
- §209: the proverb *bletë kjo, bletë ajo* kept literally: "abeille celle-ci, abeille celle-là".
- §222: *me lang e me plang*: "avec tout ce qu'elle porte".
- §246 item 4: *mos shkosha me shpirt*: "si je ne vais pas en mon âme selon les anciennes bornes", closer to the Albanian than "faithfully".
- §250: *faqes së zezë* kept literally as "la face noire" (disgrace).
- §255: *hekurin e çarkun*: "le fer et la platine" (*çark* = the firing mechanism of the gun).
- §257: *flakë per flakë* (literally "flame for flame"): "coup pour coup".
- §281 is missing from the source (it goes from §280 to §282). Kept as is, like the English.

### Terms not in the glossary (renderings chosen)

- *mëdheskë*: "maison basse" (§132).
- *çerranik i tamblit*, *koshar i drithit*: "resserre à laitage", "grenier à grain" (§140–141, §200).
- *vathë*: "enclos" (of livestock, of bees). The glossary's *xanë* is also "enclos"; context makes the difference clear.
- *këmenda*: "poil de chèvre" (§156, §167).
- *pjella*: "le croît" (for the herd), "la portée" (for the sow); *bylmet*: "laitage".
- *gjâja me pergjegje*: "le bétail avec garantie"; *pergjegje* = "garantie" all through §171–172.
- *tbâna* in §181 (the dog's post, "the dwelling of the guard"): "la demeure", not "cabane d'été", because here it is not the summer hut.
- *hunin* (§197): "le louage", to go with *kau më hu* = "bœuf de louage". *bimen* (§198): "le grain".
- *qêni shkon hupës* (§186): "le chien est perdu", modelled on *gjakhupës*.
- *peng e plak* (§185): "ni gage ni Ancien".
- *truell* (§219): "emplacement de maison"; *trolli* (§221): "terrain".
- *paperdhok*: "caillou"; *latushë (spatë)*: "la hachette (la hache)"; *spatë* alone: "hache".
- *tekë (thuper)*: "part (verge)" (§218).
- *picigiatë*: "dressées"; *landë e montueme*: "arbre marqué" (§238).
- *dishmitarë* (pebbles round the boundary stone): "témoins".
- *bûcë dheu*, *plis*: "motte de terre", "motte"; *cup të krahit*: "le haut de l'épaule".
- *ngatrresi*, *ngatrrim*: "fauteur de brouille", "brouille" (§250–251).
- *muranë*: kept in italics as *murana*, plural *muranas* (the glossary gives "murana").
- *gurapesh*: "jet de pierre"; *sà bindi*: "d'une taille monstrueuse"; *kush i del!*: "qui s'en charge !" (Section 60).
- *damçori* (§266): "le fauteur de dommage".
- *kanune Vigâjsh*: "kanuns des Géants"; *marren e korin*: "la honte et l'opprobre" (note after §266).
- *pash*: "brasse"; *pllâmbë*: "empan"; *kambë* (measure): "pied" (§267).
- *kufijar*: "voisin"; *ledh*: "levée de terre"; *strehë*: "avant-toit"; *jezull*: "surplomb"; *kmesë*: "serpe" (§267).
- *shtîja e Flamurit*: "la hampe de la Bannière" (§274).
- *udha e verbët*: "chemin aveugle"; *kapercyell*: "échalier"; *kambsorët*: "les gens à pied" (§275–276).
- *percjellsa me të dekun*: "le cortège avec le mort" (§278).
- *Malcija / Malësija e Lezhës*: "Montagne de Lezha".
- Place names in §264 and §266 follow the English: Nën-Nderfanda, Fusha të Lugjeve, Mal Shêjt, Gjokë Buça of Kaçinari, Kushneni.

## Part 04 — Book Five, Work (§289–498), source lines 1687–2250

### Uncertain readings

- §292: *shaterkazi* read as *shat e kazmë*, "la houe et le pic"; bracketed note kept as in the English.
- §319: *koshiq* left in Albanian with "[une mesure de grain]"; *pendë* glossed as in the English.
- §321: *rrshiqi, frysi, kullma* rendered "tenailles, soufflet, enclume"; *eshken* "charbon". All tentative, bracket kept.
- §322: *mabathë* rendered "reforger" (English "re-edge"); uncertain.
- §329: "une hache par dix hommes" follows the English "one axe apiece for ten men"; *kà nji spatë krye dhetë vetësh* could also mean one axe for each of ten men.
- §331: "dormir sur un coude" kept literal (sleep lightly).
- §344: proverb "Pour la boutique et le moulin, les associés ne sont pas mis à l'amende" kept literal; sense unclear.
- §353: *të shkeluna me Pleq* "parcourus avec des Anciens"; *e dâme edhè e kputme* "partagé et tranché".
- §354: "Le Kanun ne met pas Ancien sur Ancien" (one arbitration over another).
- §418: the subject of "have no right" is ambiguous in the Albanian; followed the English "[les nouveaux venus]".
- §422: *shqerth* "martres" uncertain (bracket kept).
- §437, §444–446: *perzivoj*, *kariqe*, *rrjell* left in Albanian, as in the English.
- §483: *kelbazët* "la douve", probable; the paragraph breaks off.
- §484 item 3: obscure, "[Obscur.]"; items 6 (23) and 34 (590) marked "[sic]".
- §485: second proverb "Le cheval de louage a sa peau sur la poutre", obscure.

### Departures from the English

- §303 *të çveshunt* rendered "l'effeuillage" (husking of maize) rather than a general "dépouillement".
- §378 *leçi*: the glossary gives "mise au ban"; here the word means the rule the Kanun has laid down, so I wrote "ce ban" (French *ban* = proclamation/prohibition), which keeps the glossary word.

### Terms not in the glossary (renderings chosen)

- *plang* (of a channel or house): "domaine" (to match *plangçore* = canal de domaine); §484 item 1 "le domaine ou l'emplacement de la maison".
- *âmë* (of a channel): "lit".
- *shesta* (§359, §362): "tracé".
- *shoqni* / *shokë* (channel partnership): "les associés"; *pjestàr* "participant".
- *mullîs*: "meunier"; *perbûjs*: "aubergiste".
- *farketar*: "forgeron"; *hekurishtat*: "les fers"; *të zotët e hekurishtavet*: "les maîtres des fers".
- *valanicë* (§374): "foulon".
- *shpêz* (game): "gibier"; in Section 74 "bête".
- *dorëras* in the hunting chapter: "le tueur" (the glossary's "meurtrier" is for homicide; here it is the hunter whose shot killed the game).
- *opanga*: "sandales (*opanga*)".
- *gjurmë*: "traces"; *i zoti i gjurmvet*: "le maître des traces".
- *hurdhë*: "fosse" (pool).
- *kofen, kosh*: "nasse, panier" (glossary).
- *kapàr*: "arrhes"; *e kaparueme*: "arrhée".
- *kufijar*: "voisin" (boundary neighbour).
- *Malsi*: "Hautes Terres".
- *kerçik* (§382): "une part".
- *kpucë* (§489): "souliers", in quotation marks (the fee).
- *i xêhet kryet* (§395): "n'en répond pas".

## Part 05 — notes (lines 2251–2908, §499–734)

### Structure

- The source range ends on a blank line (2908). `fr_check.py` strips trailing newlines, so the file's last line is a single space so that the part has 658 lines. Strip it when the parts are joined, if needed.
- Book Eight's heading is printed `DERA` in the source. I read it as `NDERA` and wrote "L'HONNEUR", as the English does.
- §601 is printed `§.691.` in the source (see working/notes.md). I give the correct number and add no bracket, as the English does.
- §544: the Albanian is missing its closing quotation mark. I closed it.

### Uncertain readings

- §500 *sà të dhaçë ké me më dhânë*: the persons are odd ("as much as you give, you have to give me"). I give the plain sense: "autant tu m'auras donné, autant tu auras à recevoir de moi".
- §520 *Gjuha âsht tulit*: literally "the tongue is boneless flesh" (*tul*). I wrote "est chair sans os", which is closer to the Albanian than the English "has no bone".
- Section 88, maxim *Beja làn gjaqe*: in Gheg, *laj* means both "wash" and "pay off". I wrote "Le serment lave les sangs" (the English has "pays") because it keeps the image, and *laj* in the sense "clear oneself by oath" comes back in §546–547 and §586 ("se laver"). "acquitte" would also be defensible. In §631, *Buka e làn dâmin* is clearly about paying: "Le pain paie le dommage".
- §546 *me là vendin*: probably a misprint for *vetën/vedin* ("to clear oneself"), as in §547 *Védin me e là*. Translated "se laver".
- §562 *mbë të cillen i kjàn zêmra mâ fôrt*: literally "over which his heart weeps most". I wrote "contre laquelle son cœur se plaint le plus" (the English has "suspects").
- §589 *ajo do t'a lajë*: the subject is feminine ("she/it"), maybe "the house" of the perjurer. Like the English, I wrote "le parjure"; the plural "leur imprime" that follows supports a reading as the household. *mjé në shtatë faqe* (literally "up to seven faces") became "jusqu'à la septième génération".
- §625 *do të hupish pûntorët*: *pûntorët* is literally "the workers". I kept the English "journées de travail" and added "[y mettre] de ton pain". Uncertain.
- §638 *të pasët mbetë ngiat*: unclear. I wrote "tant pis pour toi" (the English has "left in the lurch").
- §647 *e karmote më hu*: unidentified verb. I kept the English sense "chassait … sur un pieu" with its bracketed note.
- §652, note: *s'e mêrr ndore at pûnë* (literally "does not take that matter under protection"). I wrote "ne laisse pas passer cette affaire". *fiket me lang e plang* ("hound and property") became "il s'éteint corps et biens".
- §682 *me të rame diellit / me të mârrun të diellit*: literally "when the sun strikes / when the sun is taken". I kept this image and added the gloss in parentheses that the source gives.
- §692 *kasnecijet* (read as "obstinacy") and *pré presë të bame* were left as in the English: there is a bracket for the unclear words.

### Departures from the English

- §543 *të shofé bén*: "voir le serment" (literally "to see the oath"), not "receive".
- §545 *me i a mbledhë pêjt*: "tenir la bride", the image of reins kept; the same in §572.
- §583 *gisht*: "mis le doigt dans" (literally "a finger in it"), not "a hand".
- §632: in *në mik a n'anmik*, the word *mik* means "friend" because it is set against "enemy". I wrote "un ami ou un ennemi", the only exception to the rule *mik* = "hôte".

### Terms not in the glossary

- *burrni*: "honneur d'homme" (§510, §518, §615 a); *shburrnohem* "se déshonorer".
- *kuletë*: "escarcelle" (Section 84). I avoided "bourse" because the glossary gives *qese* = "bourse" (a unit of the blood price).
- *mohi*: "la dénégation" (title of Section 87, §540, §552).
- *me u dlirë*: "se purger" (of an accusation); *me u là me bé*: "se laver par le serment".
- *dorë beje* (§530, §536): "sorte de serment" in §530 (*dorë* = kind), "main du serment" in §536.
- *betarë*: "ceux qui jurent" (§536).
- *bérrêjshëm*: "le parjure"; *bé e rrêjshme*: "faux serment".
- *debeja*: "refus du serment" (§583).
- *kpucët (e Kapucarit)*: "les "souliers" de l'Informateur" (§592 b, §687), in quotation marks because this is the name of the fee.
- *derhêm*: "dirhems" (§594).
- *i pabesi*: "l'homme sans foi" (§646–648).
- *shoq*: "compagnon"; *katundi shoqi-sho'it*: "les gens d'un même village" (§651).
- *kryet e vendit*: "la place d'honneur".
- *trevezë (sofer)*: "table (*sofra*)".
- *kashata*: kept in italics, uncertain (§601 j, §663–664), as in the English.
- *rrasa e vegshit*: "la dalle de la marmite" (§601 i). *rrasë* is a stone slab, the lid of the baking pot.
- *vllaznim*: "fraternité jurée"; *kumbari*: "parrainage"; *Shengjoni*: "la parenté de Saint-Jean"; *ndrikulli*: "le lien de commère" (§709), "la visite de la commère" (§711–713).
- *krushqi* (§697, §704–710): "mariage", "s'allier par mariage".
- *nip/mesë trungu*: "neveu/nièce du tronc"; *plangu i babës*: "le domaine du père" (§702).
- *Lidhunash*: "les Jours gras" (§712).
- *gjurdi, brekë e mangore*: "une veste, un pantalon et un gilet à manches" (§731), as in the English, uncertain.
- *asper*: "aspre" (§725).

## Part 06 — translation notes (lines 2909–3554, §735–990)

### Uncertain readings

- §746: *verbue*, "blinded" (buds eaten off) → "aveuglé", kept literal as in the English.
- §749, §755: *verza (kulàr-krrabza)* → kept as *verza* with the gloss "(collier-entrave)". The English "yoke-collar" is a guess; a wooden collar/yoke that stops a pig getting through fences.
- §754: *e làn me krye* → "il a payé de sa tête", as in the English.
- §768 g, §774, §776: *bracat* and *biramelat* kept in Albanian; the English bracket ("minors and the simple-minded") is translated. §775 *mêcat* → "simples d'esprit".
- §784: *lagja lagjes* → "un quartier ... avec l'autre" (literal). The English has "one side ... the other". *lagje* can also mean "party, side" (as in §928, §940, where I give "partie").
- §795: *'si t'a leçisë pretarin e t'a lajë shpi me shpi* → "une fois que celle-ci a mis le razzieur au ban et laissé l'affaire de maison à maison". The subject is presumably the village/Banner. *leçis* is given as "mettre au ban" (glossary), not the English "proclaim".
- §799: *hànor*, *vergan* still unidentified; English bracket translated.
- §823: *aj, qi prin ase rrethas* → "celui qui mène, ou bien tous à tour de rôle"; *rrethas* is unclear.
- §840: *po kje sè duelen faqe* → "s'ils ont été vus" (follows the English); could also be "if they came out openly / were exposed".
- §842: *per presë, qi i bani* → "pour la coupure [de la *besa*] qu'il lui a faite"; *e lên në qull* → "le laisse en plan".
- §853: *nevojë uhazishte* → "un besoin que chacun se prête à son tour" (literally a "borrowing" need). *opanga* → "sandales" (*opanga*), the fee; §966–968 *kpucë* → "chaussures".
- §880: *priten në besë* → "ils sont abattus sous la *besa*" (literally "cut down in the besa").
- §883: *s'i priten miq besës ... por atij, prej shpis së të cillit duelen* → rendered "ce n'est pas la *besa* ... dont l'hôte est violé, mais la maison d'où ils sont partis". Syntax is compressed; meaning as in the English.
- §889: *rrumbull katerqind derhêm n'okë të vet* → "quatre cents drachmes rondes à son oka" (an oka = 400 dirhems; i.e. each man counts himself full weight).
- §892: *krye, plak a sterplak* → "un chef, un Ancien ou un Grand Ancien", with the English alternative in brackets.
- §894: *kerçik* kept in brackets; meaning uncertain ("measure").
- §923: *në pûnë e në mndyrë të keqe* → "dans l'action et de la mauvaise manière" (literal).
- §930: *tuj jau bâ gjakun giobë* → "en changeant leur sang en amende" (literal; it seems to mean their blood counts for nothing / is settled by the communal fine, against the rule of §916).
- §931: *të shkrihen per mnderë* → "se consumer d'effroi", following the English "melt away in terror"; uncertain.
- §942: *e shkrepmja* → "la détente pressée".
- §959: kept as printed ("encourt une amende"), with the English bracket on the probable lost negation translated.
- §971: *hutë (martine)* → *huta* (fusil Martini).
- §983: *'si të vêhet per fije* → "une fois ... mise en train" (literally "put on the thread").

### Departures from the English

- §802: the English bracket on *Shpin* is moved to the end of the paragraph so as not to break the sentence.
- §784: see above ("quartier" rather than "side").
- §939, §940, §970, §972: *dorzân* rendered "garants" (glossary "garant (du sang)") since these are the guarantors of a reconciled blood; heading of Section CXXXI "Le meurtre sous cautionnement" (*dorzani* = cautionnement). Elsewhere (§852, §853, §872, §900, §902, §925, §932, §934) *dorzân/dorzanitet* in the sense of sureties given between the two houses → "caution(s)".

### Terms missing from the glossary (renderings chosen)

- *vath* → "parc" (enclosure for flocks; "parc brisé" for *vath i thyem*). Distinct from "enclos" (*xanë/ograjë*).
- *dypernjahja* → "le deux pour un" (glossary "deux pour un").
- *grabitçar/grabitçor*, *grabitja* → "brigand", "brigandage".
- *pretar* → "razzieur".
- *cubni*, *vjedhni* → "vol"; *bracni* → "larcin".
- *gjurma* → "la trace".
- *kurthë*, *lak* → "piège", "lacet".
- *kmesë* → "serpe"; *tela/teja* → "corde" (*teja*).
- *babune* kept in Albanian (unidentified grain measure).
- *um* → "charrue" (*um*), uncertain, as in the English.
- *kadoci* kept in parenthesis with "le chanteur"; *herori (sahati)* → "l'horloge (la montre)".
- *pare të thata* → "argent sec" (cash).
- *gjaksor/gjaks* → "celui qui doit le sang".
- *kushrîni të dame zjarmit* → "cousins de feux séparés" (zjarm "fire, hearth"; glossary uses "feu" for *tym*).
- *e thame krahësh* → "privée de ses bras".
- *firuk* → "de basse naissance", opposed to *fisnik* "noble".
- *shtat e dhûnë bashkë* → "corps et déshonneur en commun".
- *i marruem(e)* → "déshonoré(e)"; *me dalë me marre* → "s'en aller dans la honte".
- *vrasa pà hiri* → "meurtre involontaire".
- *shkues i gjakut*, *shkuesija* → "entremetteur du sang", "l'entremise" (glossary *shkues* = marieur is the wedding sense; *ndermjetës* = médiateur is kept for §982).
- *i zoti i gjakut* → "le maître du sang".
- *lasin e keq* → "le mauvais drôle" (*lasi* unidentified).
- *vllaznim* → "fraternisation".
- *sqepar* → "herminette"; *prak t'eper* → "seuil supérieur"; *pregjet e krahvet* → "montants".
- *shokë* (§736) → "villageois"; §840 *shoqi* → "covillageois".

## Part 07 notes (lines 3555–4351, §991–1263)

### Uncertain readings

- §1019, §999: *zabuka* kept in Albanian and italics ("le gage de consentement, ou de *zabuka*"; "leur *zabuka*" in §999, where the English has "their consent").
- §1030: "partagés à la pierre" kept with the English bracketed guess (boundary cases, stone oath of §244–249).
- §1065: *s'kà pse shtrydhet*, "il n'y a pas à le presser" (no point squeezing the jury); could also mean "no need to wrangle".
- §1086, §1089: "la main sur le serment" for *me dorë në bé* (the promised amount is sworn to), as in the English.
- §1145: *per une zjarmi* read as "pour les fautes qui appellent le tison" (*une* = firebrand, as *unen e zjarmit* in §1197, §1199); *lima* left untranslated, with the English bracket.
- §1167: follows the English reading (the village with its Elders oppresses a clan; that clan's Elder defends it). The Albanian is ambiguous.
- §1178: "La jambe étrangère, nos têtes", literal, bracket kept; sense unknown.
- §1193: "pour la mort et pour la vie" (*gjellë* = life; may be "food"), bracket kept.
- §1194 e: "tue et disparais" for *Vra e hup*, literal.
- §1237: "ils mettront sur leur tête le col de leur veste" for *jakzat e gjurdijavet*; uncertain.
- §1244: "Que votre table soit dressée pour le bien !" for *Ju shtrofèt per të mirë!*, with the English explanatory bracket.
- Note after §1199: *kasnecija* "l'arrogance" (as in the English and the notes, not "the criers"); *me të zi* "avidement"; *deri të damët zjarmit* "jusqu'à ceux qui ont un feu séparé".

### Places where I depart from the English

- §1222–1228: the English adds a dash before the Roman numerals ("– II."); the Albanian has none, so I left it out.
- §1221 a: *telozë* is "tribut", as in §1160 ("la dîme ou le tribut"); the English has "tax" here and "tribute" in §1160.
- §1237, §1242, §1243: *miqt*, *miq*, *miqsija* are "les hôtes" (brief: *mik* is always "l'hôte"); §1242 "des hôtes [du dehors]", following the glossary's *krushq miq*. In §1243 the English has "the in-laws"; *miqsija* here is opposed to the fellow villagers, so I read it as the outside guests.
- §1251: *në dekë të mikut* "à la mort d'un ami". "Hôte" would be absurd here; this is the one place I did not use "hôte" for *mik*.
- §1260: *shpija e mikut* is "la maison de l'allié" (the daughter's in-laws), following the glossary's §56 exception ("allié").

### Terms missing from the glossary (renderings chosen)

- *opangat* (Elders' fee): "les sandales" (§1021, §1027–1028, §1040, §1042); in §1021 "les sandales, c'est-à-dire le prix de l'arbitrage".
- *kpucët* (informer's fee): "les souliers", in quotation marks at the first occurrence (§1081).
- *pritëtarët*: "examinateurs" (glossary); *kapucarija* (§1089): "le prix de l'informateur".
- *ushtri*: "la guerre" ("exempté de la guerre").
- *angari*: "corvée".
- *patalok*: "lieu d'appel" (§1213, §1215); *kushtrim*: "l'alarme" (§1217).
- *kasnec a i lajm*: "crieur ou annonceur" (§1213).
- *e premja e shpis*: "l'abattage de la maison" (§1188–1190).
- *une (e zjarmit), spatë*: "le tison, la hache".
- *kortarët*: "les bourreaux" (§1136, §1148).
- *Drekë* (funeral meal): "le repas funèbre".
- *gjâmë, gjâmatarët*: "la lamentation, ceux qui font la lamentation"; *grrishten*: "se griffent le visage".
- *Virgjinat*: "les Vierges (les femmes qui s'habillent en homme)".
- *Kreu i Flamurit*: "le Chef de la Bannière" (singular of *Krenët*, "Chefs"); *krye i Flamurit* (§1049) "un chef de Bannière".
- Book Twelve title *Shlirime e perjashtime*: "LIBÉRATIONS ET EXEMPTIONS"; verb "libère et exempte".
- *Gryka e Oroshit*: "la Gorge d'Orosh"; *Sh. Pal*: "Saint-Paul". Place names are kept as the English gives them; descriptive parts are translated (Source du Figuier, Friche de Selita, Tombes de Shala, Tilleul de l'Assemblée).

