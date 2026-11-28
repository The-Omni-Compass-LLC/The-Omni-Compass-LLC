(()=>{ /* ✝️ CULTURES & RELIGION (v238, the Cultures & Religion page of www.omni-galaxy.com): its own platform inside KAN-IN. The five largest world religions with their scriptures and
   books, every other living tradition we could document, a scripture shelf, a side-by-side comparison, holy days by month, a quiz,
   and Ask AI. Each tradition is described the way it describes itself and the way scholars record it; nothing is ranked as true or
   false. Numbers: Pew Research Center, figures for 2020 (published 2025); smaller traditions are estimates and are marked so.
   Read aloud, copy and save to Projects on every card; the reading links open the texts on public sites in a new tab. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const getLS=(k,d)=>{ try{ const v=localStorage.getItem(k); return v==null?d:JSON.parse(v); }catch(_){ return d; } };
 const putLS=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(_){ } };
 /* [title, what it is, reading link] */
 const BIG=[
 {id:'christianity',icon:'✝️',name:'Christianity',people:'2.3 billion',share:28.8,region:'Worldwide',began:'1st century CE, Judea (today Israel and the Palestinian territories)',age:2000,
  founder:'The followers of Jesus of Nazareth',god:'One God in three persons, Father, Son and Holy Spirit (the Trinity)',day:'Sunday',worship:'Church, chapel, cathedral',city:'Jerusalem, Bethlehem, Rome',
  sum:'Christians believe Jesus of Nazareth is the Son of God and the promised Messiah, that he died by crucifixion and rose from the dead, and that through him people are forgiven and reconciled with God.',
  beliefs:['Jesus’s life, death and resurrection','Salvation by God’s grace, received through faith','The two great commandments: love God and love your neighbour (Mark 12:30–31)','The Lord’s Prayer (Matthew 6:9–13)','Sacraments such as baptism and Holy Communion'],
  branches:['Catholic, about 1.3 billion, led by the Pope in Rome','Protestant: Lutheran, Reformed, Anglican, Baptist, Methodist, Pentecostal and many more','Eastern Orthodox, about 220 million','Oriental Orthodox: Coptic, Ethiopian, Eritrean, Armenian, Syriac','Other Christian bodies, among them the Latter-day Saints and Jehovah’s Witnesses'],
  books:[['The Bible','Two parts. The Old Testament: 39 books in Protestant Bibles, 46 in Catholic Bibles (with the deuterocanonical books) and more in Orthodox ones. The New Testament: 27 books.','https://www.biblegateway.com/'],
   ['The four Gospels','Matthew, Mark, Luke and John: the life, teaching, death and resurrection of Jesus.','https://www.biblegateway.com/passage/?search=Matthew+5'],
   ['Acts and the Letters','Acts tells of the first churches; 21 letters (the Epistles), many by the apostle Paul, teach the new communities; Revelation closes the Bible.','https://www.biblegateway.com/passage/?search=Romans+8'],
   ['The Psalms','150 songs and prayers shared with Judaism, the most read book of the Old Testament in Christian worship.','https://www.biblegateway.com/passage/?search=Psalm+23'],
   ['The Creeds','The Apostles’ Creed and the Nicene Creed (councils of 325 and 381 CE): the faith in a few lines, said in services worldwide.',''],
   ['Augustine, Confessions','Written about 400 CE, the first great spiritual autobiography.','https://www.gutenberg.org/ebooks/3296'],
   ['The Imitation of Christ','Thomas à Kempis, about 1420s, one of the most widely read Christian devotional books.','https://www.gutenberg.org/ebooks/1653'],
   ['Catechism of the Catholic Church','1992, the summary of Catholic teaching.',''],
   ['Book of Common Prayer','First edition 1549, the prayer book of the Anglican churches.','']],
  days:['Christmas, 25 December (many Orthodox churches keep it on 7 January)','Lent, the 40 days before Easter','Holy Week and Good Friday','Easter, a Sunday in March or April','Pentecost, seven weeks after Easter','Sunday worship every week'],
  places:['Jerusalem: the Church of the Holy Sepulchre','Bethlehem: the Church of the Nativity','Nazareth and the Sea of Galilee','Vatican City: St Peter’s Basilica','Santiago de Compostela, Lourdes and Fátima: pilgrim routes and shrines']},
 {id:'islam',icon:'☪️',name:'Islam',people:'2.0 billion',share:25.6,region:'Middle East',began:'610 CE, Mecca and Medina, Arabia',age:1400,
  founder:'The Prophet Muhammad (about 570–632 CE)',god:'One God, Allah (Arabic for “God”); tawhid, the oneness of God',day:'Friday (congregational prayer, Jumu’ah)',worship:'Mosque (masjid)',city:'Mecca, Medina, Jerusalem',
  sum:'Muslims believe the Quran is the word of God revealed to the Prophet Muhammad through the angel Gabriel, the last in a line of prophets that includes Adam, Abraham, Moses and Jesus.',
  beliefs:['The Five Pillars: the declaration of faith (shahada), prayer five times a day (salat), giving to those in need (zakat), fasting in Ramadan (sawm), the pilgrimage to Mecca once in a lifetime for those able (hajj)','The six articles of faith: God, the angels, the revealed books, the prophets, the Day of Judgement and divine decree','Submission to God’s will (the meaning of the word islam)','Prayer facing the Kaaba in Mecca'],
  branches:['Sunni, about 85 to 90 percent of Muslims','Shia, about 10 to 15 percent: Twelver, Ismaili and Zaydi','Ibadi, mainly in Oman','Sufism, the mystical path found among both Sunni and Shia'],
  books:[['The Quran','114 chapters (surahs) and about 6,236 verses (ayat) in Arabic, revealed between 610 and 632 CE and gathered into one written text under the third caliph, Uthman, about 650 CE.','https://quran.com/'],
   ['Al-Fatiha','The opening chapter, seven verses, recited in every unit of the daily prayers.','https://quran.com/1'],
   ['The Hadith','Reports of the Prophet’s words and actions. Sunni Muslims hold six major collections, led by Sahih al-Bukhari and Sahih Muslim; Shia Muslims hold the Four Books, led by al-Kafi.','https://sunnah.com/'],
   ['The Sira','Biographies of the Prophet, the earliest by Ibn Ishaq (8th century).',''],
   ['Tafsir','Commentaries that explain the Quran verse by verse, such as al-Tabari’s (10th century).',''],
   ['Nahj al-Balagha','Sermons and sayings attributed to Ali, gathered in the 10th century, especially treasured by Shia Muslims.',''],
   ['Rumi, the Masnavi','13th-century Sufi poem in Persian, about 25,000 verses.','']],
  days:['Ramadan, the month of fasting from dawn to sunset','Eid al-Fitr, the festival that ends Ramadan','Eid al-Adha, the festival of sacrifice during the Hajj','Islamic New Year and Ashura','Friday prayer every week','The Islamic calendar is lunar, so each date comes about 11 days earlier every year'],
  places:['Mecca: the Kaaba and the Masjid al-Haram','Medina: the Prophet’s Mosque','Jerusalem: the Al-Aqsa Mosque and the Dome of the Rock','Karbala and Najaf in Iraq, holy to Shia Muslims']},
 {id:'hinduism',icon:'🕉️',name:'Hinduism',people:'1.2 billion',share:14.9,region:'South Asia',began:'Roots over 3,500 years old, the Indian subcontinent (the Vedic period, about 1500 BCE)',age:3500,
  founder:'No single founder; it calls itself Sanatana Dharma, “the eternal way”',god:'Brahman, the one ultimate reality, worshipped in many forms: Vishnu, Shiva, Devi the Goddess, Ganesha, Krishna, Rama and more',day:'No single weekly day; daily worship at home and temple',worship:'Mandir (temple) and the home shrine',city:'Varanasi, Ayodhya, Vrindavan',
  sum:'Hindus seek to live by dharma, right living and duty, and over many lifetimes to reach moksha, freedom from the cycle of birth and rebirth.',
  beliefs:['Dharma: duty and right living','Karma: every action has its consequence','Samsara: the cycle of birth, death and rebirth','Moksha: liberation from that cycle','Atman, the self, and Brahman, ultimate reality','Four paths: devotion (bhakti), knowledge (jnana), selfless action (karma yoga) and meditation (raja yoga)'],
  branches:['Vaishnavism: Vishnu and his forms Krishna and Rama','Shaivism: Shiva','Shaktism: the Goddess (Devi, Durga, Kali)','Smartism: several deities as forms of one Brahman','Many regional, family and temple traditions'],
  books:[['The four Vedas','Rigveda, Samaveda, Yajurveda and Atharvaveda: hymns and rites, the oldest scriptures (shruti, “what was heard”). The Rigveda alone holds 1,028 hymns in ten books.','https://www.sacred-texts.com/hin/'],
   ['The Upanishads','Over 100 philosophical texts, about 13 of them principal, on Brahman and the self.','https://www.sacred-texts.com/hin/upan/'],
   ['The Bhagavad Gita','700 verses in 18 chapters: the god Krishna counsels the warrior Arjuna on duty, devotion and the self. Part of the Mahabharata.','https://www.holy-bhagavad-gita.org/'],
   ['The Mahabharata','Attributed to the sage Vyasa; one of the longest poems ever written, about 100,000 couplets in its longest form.','https://www.sacred-texts.com/hin/maha/'],
   ['The Ramayana','Attributed to the poet Valmiki; about 24,000 verses in seven books telling the life of Prince Rama and Sita.','https://www.sacred-texts.com/hin/rama/'],
   ['The Puranas','Eighteen major Puranas of stories, genealogies and worship, among them the Bhagavata Purana.',''],
   ['The Yoga Sutras of Patanjali','196 short sutras on the practice of yoga and meditation.',''],
   ['Ramcharitmanas','Tulsidas, 16th century: the Rama story retold in Awadhi, sung across north India.','']],
  days:['Diwali, the festival of lights, October or November','Holi, the spring festival of colours, usually March','Navaratri and Durga Puja, autumn','Janmashtami, Krishna’s birth, August or September','Maha Shivaratri, February or March','Kumbh Mela, the great pilgrimage gathering on the sacred rivers','Dates follow a lunisolar calendar, so they move each year'],
  places:['Varanasi and the River Ganges','Ayodhya, Vrindavan and Mathura','Tirupati, Puri and Kedarnath','Angkor Wat in Cambodia, built as a Hindu temple in the 12th century']},
 {id:'buddhism',icon:'☸️',name:'Buddhism',people:'324 million',share:4.1,region:'East Asia',began:'About the 5th century BCE, northern India and Nepal',age:2500,
  founder:'Siddhartha Gautama, the Buddha, “the awakened one”',god:'No creator God at the centre; the goal is awakening (nirvana). Many traditions honour buddhas and bodhisattvas.',day:'Observance days on the moon’s phases (uposatha)',worship:'Temple, monastery, stupa, meditation hall',city:'Bodh Gaya, Lumbini, Lhasa',
  sum:'Buddhists follow the Buddha’s teaching, the Dharma, to end suffering through wisdom, ethical living and meditation.',
  beliefs:['The Four Noble Truths: suffering exists; it has a cause, craving; it can end; and there is a path that ends it','The Noble Eightfold Path: right view, intention, speech, action, livelihood, effort, mindfulness and concentration','The Three Jewels: the Buddha, the Dharma and the Sangha (the community)','Karma and rebirth','The Five Precepts: no killing, stealing, sexual misconduct, false speech or intoxicants'],
  branches:['Theravada: Sri Lanka, Thailand, Myanmar, Cambodia, Laos','Mahayana: China, Japan, Korea, Vietnam, including Zen and Pure Land','Vajrayana: Tibet, Bhutan, Mongolia'],
  books:[['The Pali Canon (Tipitaka)','The “three baskets”: the Vinaya (rules for monks and nuns), the Suttas (the Buddha’s discourses) and the Abhidhamma (analysis). First written down in Sri Lanka in the 1st century BCE.','https://suttacentral.net/'],
   ['The Dhammapada','423 verses in 26 chapters, the best-known collection of the Buddha’s sayings.','https://suttacentral.net/dhp'],
   ['The Lotus Sutra','Central Mahayana scripture teaching that every being can become a buddha.',''],
   ['The Heart Sutra','A few hundred words on emptiness, chanted daily across East Asia.',''],
   ['The Diamond Sutra','A printed copy dated 868 CE, found at Dunhuang, is the oldest dated printed book known.','https://www.bl.uk/collection-items/the-diamond-sutra'],
   ['The Kangyur and Tengyur','The Tibetan canon: the Buddha’s words and the great commentaries.',''],
   ['The Tibetan Book of the Dead','The Bardo Thodol, a guide read to the dying and the dead.',''],
   ['Shantideva, The Way of the Bodhisattva','8th century, a guide to the life of compassion.','']],
  days:['Vesak: the Buddha’s birth, awakening and passing, at the full moon of April or May','Magha Puja and Asalha Puja','Losar, the Tibetan New Year','Obon in Japan, honouring ancestors','Uposatha observance days each lunar month'],
  places:['Lumbini, Nepal: the Buddha’s birthplace','Bodh Gaya, India: where he awoke under the Bodhi tree','Sarnath: his first teaching','Kushinagar: his passing','Borobudur (Indonesia), the Shwedagon Pagoda (Myanmar), the Potala Palace (Lhasa)']},
 {id:'judaism',icon:'✡️',name:'Judaism',people:'14.8 million',share:0.2,region:'Middle East',began:'Ancient Israel, about 3,000 to 4,000 years ago',age:3500,
  founder:'Traced to Abraham and the covenant; the Torah given through Moses at Mount Sinai',god:'One God. The Shema: “Hear, O Israel: the LORD our God, the LORD is one” (Deuteronomy 6:4)',day:'Shabbat, Friday sunset to Saturday night',worship:'Synagogue (shul) and the home',city:'Jerusalem',
  sum:'Judaism is the religion of the Jewish people, built on the covenant between God and Israel and on living by the Torah’s commandments. Small in number, it is the root from which Christianity and Islam grew.',
  beliefs:['One God and the covenant with the people of Israel','The 613 commandments (mitzvot) of the Torah','Shabbat, the weekly day of rest','Justice, charity (tzedakah) and repairing the world (tikkun olam)','Study and debate of the texts as worship','The hope of a messianic age'],
  branches:['Orthodox, including Haredi and Modern Orthodox','Conservative (Masorti)','Reform','Reconstructionist','Ashkenazi, Sephardi and Mizrahi heritage'],
  books:[['The Tanakh (Hebrew Bible)','24 books in three parts: Torah (teaching), Nevi’im (prophets) and Ketuvim (writings). The name is made from their first letters.','https://www.sefaria.org/texts/Tanakh'],
   ['The Torah','The five books of Moses: Genesis, Exodus, Leviticus, Numbers, Deuteronomy. Read in the synagogue from a handwritten scroll, the whole of it each year.','https://www.sefaria.org/Genesis.1'],
   ['The Talmud','The Mishnah, compiled about 200 CE by Rabbi Judah ha-Nasi, with the Gemara’s discussion of it. The Babylonian Talmud was completed about 500 CE; there is also a Jerusalem Talmud.','https://www.sefaria.org/texts/Talmud'],
   ['Pirkei Avot','“Ethics of the Fathers”, the Mishnah’s book of wisdom sayings.','https://www.sefaria.org/Pirkei_Avot.1'],
   ['The Midrash','Commentary and story that open up the meaning of the Bible.',''],
   ['The Siddur','The prayer book for daily, Shabbat and festival prayer.',''],
   ['Mishneh Torah','Maimonides’ code of Jewish law, about 1170 to 1180.',''],
   ['Shulchan Aruch','Joseph Karo’s code of Jewish law, printed 1565.',''],
   ['The Zohar','The central text of Kabbalah, Jewish mysticism, which appeared in 13th-century Spain.','']],
  days:['Shabbat every week','Rosh Hashanah, the new year, September or October','Yom Kippur, the Day of Atonement, ten days later','Sukkot, the festival of booths','Passover (Pesach), spring','Shavuot, Hanukkah (December) and Purim','A lunisolar calendar, so dates move against the Gregorian one'],
  places:['Jerusalem: the Western Wall, the remaining wall of the Second Temple’s mount','Hebron: the Cave of the Patriarchs','Safed and Tiberias','Mount Sinai, by tradition']}];
 const OTH=[
 {id:'sikhism',icon:'☬',name:'Sikhism',people:'about 25 to 30 million (estimate)',region:'South Asia',age:550,began:'1469, the Punjab',founder:'Guru Nanak (1469–1539) and the nine Gurus after him',
  sum:'One God (Ik Onkar), equality of all people, honest work, sharing and service (seva). Initiated Sikhs keep the Five Ks, among them uncut hair and the steel bracelet (kara).',
  books:[['Guru Granth Sahib','1,430 pages (angs). Compiled as the Adi Granth by Guru Arjan in 1604 and declared the eternal Guru by Guru Gobind Singh in 1708; it holds hymns of six Gurus and of Hindu and Muslim saints.','https://www.searchgurbani.com/'],['Japji Sahib','Guru Nanak’s morning prayer, the opening of the Granth.',''],['Dasam Granth','Writings attributed to Guru Gobind Singh.','']],
  days:['Vaisakhi (April): the founding of the Khalsa in 1699','Gurpurabs: the Gurus’ anniversaries','Bandi Chhor Divas, with Diwali'],places:['Harmandir Sahib, the Golden Temple, Amritsar','Nankana Sahib, Guru Nanak’s birthplace','Every gurdwara’s langar, a free kitchen open to all']},
 {id:'taoism',icon:'☯️',name:'Taoism (Daoism)',people:'estimates vary widely; many practise it alongside folk religion and Buddhism',region:'East Asia',age:2400,began:'About the 4th century BCE onward, China',founder:'Laozi (traditional author of the Tao Te Ching) and Zhuangzi',
  sum:'Living in harmony with the Tao, the Way behind all things: simplicity, effortless action (wu wei), balance of yin and yang, long life and care of the body.',
  books:[['Tao Te Ching','81 short chapters, about 5,000 Chinese characters, among the most translated books in the world.','https://ctext.org/dao-de-jing'],['Zhuangzi','Stories and parables, including the famous butterfly dream.','https://ctext.org/zhuangzi'],['The Daozang','The Taoist canon; its Ming dynasty edition of 1445 holds about 1,500 texts.',''],['I Ching','The Book of Changes, shared with Confucianism.','https://ctext.org/book-of-changes']],
  days:['Chinese New Year and the Lantern Festival','Laozi’s birthday','Temple festivals of the immortals'],places:['Mount Wudang','Mount Tai and the other sacred mountains','White Cloud Temple, Beijing']},
 {id:'confucianism',icon:'📜',name:'Confucianism',people:'a way of life rather than a membership; it shaped China, Korea, Japan and Vietnam',region:'East Asia',age:2500,began:'5th century BCE, China',founder:'Confucius (Kong Fuzi, 551–479 BCE)',
  sum:'Humaneness (ren), right conduct and ritual (li), respect for parents and elders (filial piety), learning and good government.',
  books:[['The Analects','Sayings of Confucius gathered by his students.','https://ctext.org/analects'],['The Four Books','The Analects, the Mencius, the Great Learning and the Doctrine of the Mean.','https://ctext.org/mengzi'],['The Five Classics','The Book of Songs, the Book of Documents, the Book of Rites, the I Ching and the Spring and Autumn Annals.','']],
  days:['Confucius’s birthday, kept as Teachers’ Day in Taiwan on 28 September','Ancestor rites at Qingming'],places:['The Temple of Confucius and the Kong family mansion, Qufu']},
 {id:'shinto',icon:'⛩️',name:'Shinto',people:'many Japanese take part, often alongside Buddhism; membership is hard to count',region:'East Asia',age:1500,began:'Ancient Japan, no founder',founder:'None',
  sum:'Reverence for the kami, the sacred powers in nature, places and ancestors; purity, gratitude and the life of the local shrine.',
  books:[['Kojiki','“Record of Ancient Matters”, 712 CE: the creation of Japan and the kami.','https://www.sacred-texts.com/shi/kj/'],['Nihon Shoki','“Chronicles of Japan”, 720 CE.',''],['Engishiki','927 CE, the court’s book of rites and prayers.','']],
  days:['Hatsumode, the first shrine visit of the New Year','Shichi-Go-San, for children aged three, five and seven','Local matsuri festivals'],places:['Ise Grand Shrine','Fushimi Inari Taisha, Kyoto','Izumo Taisha','Meiji Shrine, Tokyo']},
 {id:'jainism',icon:'🤚',name:'Jainism',people:'about 4 to 6 million (estimate)',region:'South Asia',age:2500,began:'Ancient India; Mahavira lived in the 6th to 5th century BCE',founder:'Mahavira, the 24th Tirthankara (“ford-maker”)',
  sum:'Non-violence to every living being (ahimsa), many-sidedness of truth (anekantavada) and non-attachment (aparigraha). Two main communities, Svetambara and Digambara.',
  books:[['The Agamas','The canonical scriptures; the Svetambara canon counts 45 texts.',''],['Tattvartha Sutra','Umaswati’s summary of Jain teaching, accepted by every Jain community.',''],['Kalpa Sutra','The lives of the Tirthankaras, read during Paryushana.','https://www.sacred-texts.com/jai/sbe22/']],
  days:['Paryushana, the festival of forgiveness','Mahavir Jayanti, March or April','Diwali, Mahavira’s liberation'],places:['Palitana and the Shatrunjaya hills','Shravanabelagola and its statue of Bahubali','Ranakpur and the Dilwara temples at Mount Abu']},
 {id:'bahai',icon:'✴️',name:'Bahá’í Faith',people:'about 5 to 8 million (the community’s figures)',region:'Worldwide',age:180,began:'1844 to 1863, Persia',founder:'Bahá’u’lláh (1817–1892), heralded by the Báb',
  sum:'The oneness of God, of religion and of humanity; the equality of women and men; the harmony of science and religion; world peace.',
  books:[['Kitáb-i-Aqdas','“The Most Holy Book”, written by Bahá’u’lláh about 1873.','https://www.bahai.org/library/'],['Kitáb-i-Íqán','“The Book of Certitude”.',''],['The Hidden Words','Short verses of spiritual counsel.','']],
  days:['Naw-Rúz, the new year at the March equinox','Riḍván, 21 April to 2 May','The Twin Holy Birthdays'],places:['The Bahá’í World Centre in Haifa and Acre, with the Shrine of the Báb','The Lotus Temple, New Delhi']},
 {id:'zoroastrianism',icon:'🔥',name:'Zoroastrianism',people:'about 110,000 to 200,000 (estimate), many of them Parsis in India',region:'Middle East',age:3000,began:'Ancient Iran; dates for its prophet range from about 1500 to 500 BCE',founder:'Zarathustra (Zoroaster)',
  sum:'Ahura Mazda, the wise lord; the choice between good and evil; “good thoughts, good words, good deeds”. Fire is a symbol of purity.',
  books:[['The Avesta','The scripture; its oldest part is the Gathas, 17 hymns attributed to Zarathustra.','https://www.avesta.org/'],['The Yasna','The main liturgy, which contains the Gathas.',''],['Khordeh Avesta','Daily prayers for lay people.','']],
  days:['Nowruz, the new year at the March equinox','The six Gahambar seasonal feasts','Khordad Sal, Zarathustra’s birthday'],places:['Fire temples (Atash Behram) at Udvada, India, and Yazd, Iran']},
 {id:'folk',icon:'🏮',name:'Chinese folk religion',people:'hundreds of millions take part (estimates vary)',region:'East Asia',age:3000,began:'Ancient China',founder:'None',
  sum:'Honouring ancestors, local gods such as Mazu and Guan Yu, festivals, offerings and feng shui, often mixed with Taoism and Buddhism.',
  books:[['No single scripture','Almanacs (the Tong Shu), temple texts and “morality books” (shanshu) guide practice.','']],
  days:['Chinese New Year','Qingming, tomb-sweeping day','The Ghost Festival','The Mid-Autumn Festival'],places:['Mazu temples, beginning on Meizhou Island','Local temples in every town']},
 {id:'indigenous',icon:'🌍',name:'Indigenous and traditional religions',people:'many millions worldwide; the oldest living traditions',region:'Worldwide',age:10000,began:'Prehistory to today',founder:'None',
  sum:'Religions of a people and a land: the Yoruba orisha tradition of West Africa (carried to the Americas as Santería or Lucumí and Candomblé), Native American traditions, Aboriginal Australian spirituality (the Dreaming), Māori, Sámi and Siberian traditions, and many more.',
  books:[['Mostly oral','Teaching passes by story, song, ceremony and elders rather than a written book.',''],['Odù Ifá','The 256 odù of the Yoruba Ifá system, recited by its priests (babalawo); proclaimed by UNESCO a masterpiece of oral heritage in 2005.',''],['Popol Vuh','The K’iche’ Maya story of creation, written down in the 16th century.','https://www.sacred-texts.com/nam/pvuheng.htm']],
  days:['Seasonal and harvest ceremonies','Solstice and new-moon rites','Yoruba Odun festivals'],places:['Osun-Osogbo Sacred Grove, Nigeria','Uluru, Australia']},
 {id:'lds',icon:'✝️',name:'Latter-day Saints',people:'about 17 million members (the church’s figure; counted within Christianity)',region:'Americas',age:195,began:'1830, New York, United States',founder:'Joseph Smith',
  sum:'A Christian restorationist church that holds further scripture beside the Bible.',
  books:[['The Book of Mormon','Published 1830.','https://www.churchofjesuschrist.org/study/scriptures'],['Doctrine and Covenants','Revelations to the church.',''],['Pearl of Great Price','Further writings.','']],
  days:['General Conference, April and October'],places:['Salt Lake Temple, Utah']},
 {id:'rastafari',icon:'🦁',name:'Rastafari',people:'estimates range up to about 1 million',region:'Americas',age:95,began:'1930s, Jamaica',founder:'Grew from the crowning of Haile Selassie I of Ethiopia in 1930',
  sum:'Faith in Jah, the dignity of Africa and its diaspora, natural living (ital), and resistance to “Babylon”, the system of oppression.',
  books:[['The Bible','Read with particular weight on the Old Testament.',''],['Kebra Nagast','14th-century Ethiopian epic of the Queen of Sheba and Solomon.',''],['The Holy Piby','1920s text read by early Rastafari.','']],
  days:['Groundation Day, 21 April (Haile Selassie’s visit to Jamaica, 1966)','Ethiopian Christmas, 7 January'],places:['Shashamane, Ethiopia','Jamaica']},
 {id:'druze',icon:'⭐',name:'Druze faith',people:'about 1 million (estimate)',region:'Middle East',age:1000,began:'11th century, Egypt',founder:'Grew from an Ismaili movement',
  sum:'A closed community of faith with its own teaching on the oneness of God, living mainly in Lebanon, Syria, Israel and Jordan.',
  books:[['The Epistles of Wisdom','Rasa’il al-Hikma, the community’s scripture.','']],days:['Eid al-Adha, kept in its own way'],places:['The shrine of Nabi Shu’ayb, Galilee']},
 {id:'yazidi',icon:'🦚',name:'Yazidism',people:'about 700,000 to 1 million (estimate)',region:'Middle East',age:900,began:'Northern Iraq; reformed in the 12th century',founder:'Sheikh Adi ibn Musafir is its great saint',
  sum:'One God and seven holy beings led by Tawûsî Melek, the Peacock Angel. Faith passes by birth and oral hymn.',
  books:[['The qewls','Sacred hymns passed down orally by hereditary singers.','']],days:['Yazidi New Year (Çarşema Sor), in April'],places:['Lalish, the holy valley in northern Iraq']},
 {id:'mandaean',icon:'💧',name:'Mandaeism',people:'about 60,000 to 100,000 (estimate)',region:'Middle East',age:1900,began:'Ancient Mesopotamia',founder:'They revere John the Baptist as a great teacher',
  sum:'A gnostic faith of light and life; frequent baptism in flowing water.',books:[['Ginza Rabba','“The Great Treasure”, the main scripture.','']],days:['Parwanaya, the five-day festival of creation'],places:['Rivers of southern Iraq and Iran']},
 {id:'samaritan',icon:'📜',name:'Samaritanism',people:'about 900 people',region:'Middle East',age:2500,began:'Ancient Israel',founder:'Traces itself to the Israelites who stayed in the land',
  sum:'One of the smallest and oldest faiths: the Torah alone, worship on Mount Gerizim.',books:[['The Samaritan Pentateuch','Their own text of the five books of Moses in the old Hebrew script.','']],days:['Passover sacrifice on Mount Gerizim'],places:['Mount Gerizim, near Nablus']},
 {id:'caodai',icon:'👁️',name:'Cao Đài',people:'about 2 to 4 million (estimate)',region:'East Asia',age:100,began:'1926, Vietnam',founder:'Ngô Văn Chiêu and others',
  sum:'A faith that honours the teachers of many religions under one Supreme Being, symbolised by the Divine Eye.',books:[['The Holy Scriptures of Cao Đài','Messages received at séances in the 1920s.','']],days:['Festival of the Supreme Being, ninth day of the first lunar month'],places:['The Holy See at Tây Ninh']},
 {id:'tenrikyo',icon:'🌸',name:'Tenrikyo',people:'about 1 to 2 million (estimate)',region:'East Asia',age:190,began:'1838, Japan',founder:'Nakayama Miki',
  sum:'God the Parent, who created people to live the “Joyous Life” of helping one another.',books:[['Ofudesaki','“The Tip of the Writing Brush”, Nakayama Miki’s verses.','']],days:['Grand Service, 26 January and 26 October'],places:['The church headquarters, Tenri, Nara']},
 {id:'pagan',icon:'🌙',name:'Wicca and modern Paganism',people:'estimates vary; growing in Europe and the Americas',region:'Europe',age:75,began:'20th century, Britain and beyond',founder:'Wicca: Gerald Gardner, 1950s; many Pagan paths have no founder',
  sum:'Reverence for nature, the cycle of the seasons, and in many paths a goddess and a god.',books:[['The Book of Shadows','A personal or coven book of rites, not one fixed text.','']],days:['The eight sabbats: Samhain, Yule, Imbolc, Ostara, Beltane, Litha, Lughnasadh and Mabon'],places:['Stonehenge at the solstices']},
 {id:'none',icon:'🔭',name:'No religion (the unaffiliated)',people:'1.9 billion, 24.2% (not a religion; counted for the full picture)',region:'Worldwide',age:0,began:'Today the world’s third-largest group after Christians and Muslims',founder:'None',
  sum:'Atheists, agnostics and people who say “nothing in particular”. Many still hold spiritual beliefs or keep family customs.',books:[['No scripture','Many draw on philosophy, science and humanist writing.','']],days:['None shared'],places:['None shared']}];
 const ALL=[...BIG,...OTH];
 const MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];
 const HOLY=[[1,'✝️','Orthodox Christmas','7 January in churches on the Julian calendar'],[1,'✝️','Epiphany','6 January'],[1,'🕉️','Makar Sankranti','about 14 January, a solar festival'],[1,'🏮','Lunar New Year','late January or February; moves'],
  [2,'🏮','Lunar New Year','if it falls late'],[2,'🕉️','Maha Shivaratri','February or March; moves'],[2,'☪️','Ramadan begins','in 2026 and 2027 in February; moves about 11 days earlier each year'],[2,'✝️','Ash Wednesday, Lent begins','February or March; moves'],[2,'☸️','Magha Puja','February or March; moves'],
  [3,'🕉️','Holi','usually March'],[3,'🔥','Nowruz and Naw-Rúz','the March equinox, about 20 or 21 March'],[3,'✡️','Purim','February or March'],[3,'☪️','Eid al-Fitr','in 2026 and 2027 in March; moves'],[3,'✝️','Easter','March or April'],
  [4,'✡️','Passover','March or April'],[4,'☬','Vaisakhi','13 or 14 April'],[4,'✴️','Riḍván','21 April to 2 May'],[4,'🤚','Mahavir Jayanti','March or April'],[4,'🦁','Groundation Day','21 April'],[4,'🦚','Yazidi New Year','in April'],
  [5,'☸️','Vesak','the full moon of April, May or June'],[5,'✡️','Shavuot','May or June'],[5,'✝️','Pentecost','May or June'],[5,'☪️','Eid al-Adha','in 2026 in late May; moves'],
  [6,'☪️','Islamic New Year and Ashura','in 2026 in June; moves'],[6,'🌙','Litha, midsummer','about 21 June'],
  [7,'☸️','Asalha Puja','July'],[7,'☸️','Obon','mid-July or mid-August by region'],
  [8,'🕉️','Janmashtami','August or September'],[8,'🕉️','Ganesh Chaturthi','August or September'],[8,'🤚','Paryushana','August or September'],
  [9,'✡️','Rosh Hashanah and Yom Kippur','September or October'],[9,'🕉️','Navaratri','September or October'],[9,'📜','Teachers’ Day for Confucius','28 September in Taiwan'],
  [10,'✡️','Sukkot and Simchat Torah','September or October'],[10,'🕉️','Diwali','October or November'],[10,'🌙','Samhain','31 October'],
  [11,'✝️','All Saints’ Day','1 November'],[11,'☬','Guru Nanak Gurpurab','November, at the full moon of Kartik'],[11,'☬','Bandi Chhor Divas','with Diwali'],[11,'✝️','Advent begins','late November or early December'],
  [12,'✝️','Christmas','25 December'],[12,'✡️','Hanukkah','November or December'],[12,'☸️','Bodhi Day','8 December in Japan'],[12,'🌙','Yule','the December solstice']];
 const QUIZ=[['How many chapters (surahs) does the Quran have?',['114','99','150','66'],0],['Which book holds Krishna’s counsel to Arjuna?',['The Bhagavad Gita','The Lotus Sutra','The Analects','The Avesta'],0],
  ['How many books are in the New Testament?',['27','39','24','66'],0],['What are the five books of Moses called in Judaism?',['The Torah','The Talmud','The Zohar','The Midrash'],0],
  ['Where did the Buddha awaken?',['Bodh Gaya','Lumbini','Mecca','Varanasi'],0],['Which scripture is the living Guru of the Sikhs?',['Guru Granth Sahib','Dasam Granth','The Vedas','Kitáb-i-Aqdas'],0],
  ['The Tao Te Ching has how many chapters?',['81','114','18','27'],0],['Which is the oldest dated printed book known?',['A copy of the Diamond Sutra, 868 CE','The Gutenberg Bible','The Book of Kells','The Kojiki'],0],
  ['Which religion has the most followers?',['Christianity','Islam','Hinduism','Buddhism'],0],['The Kojiki and Nihon Shoki belong to which tradition?',['Shinto','Taoism','Jainism','Zoroastrianism'],0],
  ['How many verses does the Dhammapada have?',['423','700','1,028','6,236'],0],['Who compiled the Mishnah, about 200 CE?',['Rabbi Judah ha-Nasi','Maimonides','Joseph Karo','Rashi'],0]];
 let tab=getLS('kanin-relig-tab','big'), pick=getLS('kanin-relig-pick',''), sort=getLS('kanin-relig-sort','size'), reg=getLS('kanin-relig-reg','all'), mon=getLS('kanin-relig-mon',new Date().getMonth()+1), q='', qi=0, qs=0, qa=0, busy=null, sample=null, aiAns='';
 (async()=>{ try{ if(window.claude&&claude.use) sample=await claude.use('sample'); }catch(_){ sample=null; } })();
 const css=document.createElement('style'); css.textContent=`
#kRelig{position:fixed;inset:0;z-index:9700;overflow:auto;color:#f4ecdc;background:radial-gradient(ellipse at 50% -20%,#3b2a5c 0,#151027 45%,#0a0816 100%);padding:14px 16px calc(230px + env(safe-area-inset-bottom,0px));padding-right:calc(var(--kRailW,58px) + 16px);font:15px/1.6 system-ui,sans-serif}
#kRelig[hidden]{display:none!important}
#kRelig .rgIn{max-width:980px;margin:0 auto}
#kRelig .rgBrand{font:700 11.5px ui-monospace,monospace;letter-spacing:.1em;color:#d9b45a;text-transform:uppercase}
#kRelig h2{font:800 clamp(26px,5.5vw,40px)/1.15 Georgia,'Times New Roman',serif;color:#ffd76a;margin:8px 0 4px;text-wrap:balance}
#kRelig h3{font:800 20px/1.3 Georgia,serif;color:#fff;margin:0 0 4px}
#kRelig h4{font:800 13px system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#d9b45a;margin:12px 0 4px}
#kRelig .rgSub{color:#cdbfe6;font-size:14px;margin:0 0 10px}
#kRelig .rgTabs{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}
#kRelig .rgTabs button{min-height:42px!important;border-radius:12px!important;padding:4px 12px!important;font:800 14px system-ui,sans-serif!important}
#kRelig .rgTabs button[aria-pressed="true"]{background:#ffd76a!important;color:#1a1030!important}
#kRelig .rgCtl{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:6px 0 12px}
#kRelig .rgCtl select,#kRelig .rgCtl input{min-height:40px;border-radius:10px;font:600 14px system-ui,sans-serif;padding:4px 8px;max-width:100%}
#kRelig .rgCtl input{flex:1 1 220px}
#kRelig .rgGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:12px}
#kRelig .rgCard{background:rgba(255,255,255,.05);border:1px solid rgba(255,215,106,.25);border-radius:16px;padding:14px;min-width:0}
#kRelig .rgCard .rgIco{font-size:34px;line-height:1}
#kRelig .rgStat{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin:4px 0}
#kRelig .rgStat b{font:800 22px Georgia,serif;color:#ffd76a}
#kRelig .rgBar{height:8px;border-radius:6px;background:rgba(255,255,255,.12);overflow:hidden;margin:4px 0 8px}
#kRelig .rgBar i{display:block;height:100%;background:linear-gradient(90deg,#d9b45a,#ffd76a)}
#kRelig ul{margin:4px 0 8px;padding-left:20px}
#kRelig li{margin:2px 0}
#kRelig .rgBook{border-top:1px solid rgba(255,255,255,.1);padding:8px 0}
#kRelig .rgBook b{color:#fff}
#kRelig .rgRow{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
#kRelig .rgRow button{min-height:38px!important;padding:4px 10px!important;border-radius:10px!important;font:700 13px system-ui,sans-serif!important}
#kRelig a{color:#9fdcff}
#kRelig .rgTbl{overflow-x:auto;border:1px solid rgba(255,215,106,.25);border-radius:12px}
#kRelig table{border-collapse:collapse;min-width:760px;width:100%;font-size:13.5px}
#kRelig th,#kRelig td{border-bottom:1px solid rgba(255,255,255,.1);padding:8px;text-align:left;vertical-align:top}
#kRelig th{color:#ffd76a;background:rgba(0,0,0,.25);position:sticky;top:0}
#kRelig .rgNote{font-size:12.5px;color:#b9add3;line-height:1.5}
#kRelig .rgQ button.opt{display:block;width:100%;text-align:left;margin:6px 0;min-height:44px!important;border-radius:12px!important;font:700 15px system-ui,sans-serif!important}
#kRelig .rgQ button.ok{background:#137a3f!important}#kRelig .rgQ button.no{background:#8a1c2c!important}
#kRelig textarea{width:100%;min-height:80px;border-radius:12px;font:15px system-ui,sans-serif;padding:8px;box-sizing:border-box}
#kRelig .rgAns{white-space:pre-wrap;background:rgba(0,0,0,.3);border-radius:12px;padding:12px;margin-top:8px;min-height:24px}
@media (max-width:560px){ #kRelig .rgGrid{grid-template-columns:minmax(0,1fr)} #kRelig h2{font-size:26px} }`; document.head.appendChild(css);
 function box(){ let d=$('kRelig'); if(d) return d; d=document.createElement('div'); d.id='kRelig'; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Cultures and Religion'); d.hidden=true; document.body.appendChild(d);
  d.addEventListener('click',onClick); d.addEventListener('change',onChange); d.addEventListener('input',e=>{ if(e.target.dataset.rg==='q'){ q=e.target.value; paintBody(); } }); return d; }
 const byId=id=>ALL.find(r=>r.id===id);
 const words=r=>(r.name+' '+(r.sum||'')+' '+(r.books||[]).map(b=>b[0]+' '+b[1]).join(' ')+' '+(r.region||'')+' '+(r.founder||'')+' '+(r.places||[]).join(' ')).toLowerCase();
 const match=r=>{ if(reg!=='all'&&r.region!==reg) return false; if(pick&&r.id!==pick) return false; const t=q.trim().toLowerCase(); return !t||t.split(/\s+/).every(w=>words(r).includes(w)); };
 const sorted=L=>{ const s=L.slice(); const size=r=>r.share!=null?r.share:(r.id==='none'?24.2:0); if(sort==='size') s.sort((a,b)=>size(b)-size(a)); else if(sort==='age') s.sort((a,b)=>(b.age||0)-(a.age||0)); else if(sort==='az') s.sort((a,b)=>a.name.localeCompare(b.name)); else if(sort==='region') s.sort((a,b)=>(a.region||'').localeCompare(b.region||'')||a.name.localeCompare(b.name)); else if(sort==='books') s.sort((a,b)=>(b.books||[]).length-(a.books||[]).length); return s; };
 const link=(u,t)=>u&&/^https:\/\//.test(u)?' <a href="'+esc(u)+'" target="_blank" rel="noopener">'+esc(t||'Read it online ↗')+'</a>':'';
 const acts=(id)=>'<div class="rgRow"><button type="button" data-rg="read" data-id="'+id+'" data-noul>🔊 Read aloud</button><button type="button" data-rg="stop" data-noul>⏹ Stop</button><button type="button" data-rg="copy" data-id="'+id+'" data-noul>📋 Copy</button><button type="button" data-rg="save" data-id="'+id+'" data-noul>📁 Save</button><button type="button" data-rg="ask" data-id="'+id+'" data-noul>🤖 Ask AI</button></div>';
 function bigCard(r){ return '<div class="rgCard"><div class="rgIco">'+r.icon+'</div><h3>'+esc(r.name)+'</h3><div class="rgStat"><b>'+esc(r.people)+'</b><span>'+r.share+'% of the world</span></div><div class="rgBar"><i style="width:'+Math.max(1,Math.min(100,r.share/28.8*100))+'%"></i></div>'+
  '<p>'+esc(r.sum)+'</p><h4>Began</h4><p>'+esc(r.began)+'. '+esc(r.founder)+'.</p><h4>God</h4><p>'+esc(r.god)+'</p><h4>What they believe</h4><ul>'+r.beliefs.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul><h4>Branches</h4><ul>'+r.branches.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>'+
  '<h4>Scriptures and books ('+r.books.length+')</h4>'+r.books.map(b=>'<div class="rgBook"><b>📖 '+esc(b[0])+'</b><br>'+esc(b[1])+link(b[2])+'</div>').join('')+
  '<h4>Holy days</h4><ul>'+r.days.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul><h4>Holy places</h4><ul>'+r.places.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul><p class="rgNote">Worship: '+esc(r.worship)+' · Weekly: '+esc(r.day)+'</p>'+acts(r.id)+'</div>'; }
 function othCard(r){ return '<div class="rgCard"><div class="rgIco">'+r.icon+'</div><h3>'+esc(r.name)+'</h3><div class="rgStat"><span>'+esc(r.people)+'</span></div><p>'+esc(r.sum)+'</p><h4>Began</h4><p>'+esc(r.began)+(r.founder&&r.founder!=='None'?'. '+esc(r.founder):'')+'.</p>'+
  '<h4>Scriptures and books ('+r.books.length+')</h4>'+r.books.map(b=>'<div class="rgBook"><b>📖 '+esc(b[0])+'</b><br>'+esc(b[1])+link(b[2])+'</div>').join('')+'<h4>Holy days</h4><ul>'+(r.days||[]).map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul><h4>Holy places</h4><ul>'+(r.places||[]).map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>'+acts(r.id)+'</div>'; }
 function paintBody(){ const B=$('rgBody'); if(!B) return; let h='';
  if(tab==='big'){ const L=sorted(BIG.filter(match)); h='<p class="rgSub">The five largest world religions by followers. Together they hold about 73% of the world’s people.</p><div class="rgGrid">'+(L.map(bigCard).join('')||'<p>Nothing matches. Clear the search or the filters.</p>')+'</div>'; }
  else if(tab==='all'){ const L=sorted(ALL.filter(match)); h='<p class="rgSub">'+L.length+' of '+ALL.length+' traditions shown. The five largest are first under “Largest first”.</p><div class="rgGrid">'+(L.map(r=>BIG.includes(r)?bigCard(r):othCard(r)).join('')||'<p>Nothing matches.</p>')+'</div>'; }
  else if(tab==='shelf'){ const rows=[]; sorted(ALL.filter(r=>reg==='all'||r.region===reg)).forEach(r=>{ if(pick&&r.id!==pick) return; (r.books||[]).forEach((b,i)=>{ const t=q.trim().toLowerCase(); if(t&&!t.split(/\s+/).every(w=>(b[0]+' '+b[1]+' '+r.name).toLowerCase().includes(w))) return; rows.push([r,b,i]); }); });
   h='<p class="rgSub">'+rows.length+' scriptures and books. Search a title: Quran, Gita, Torah, Talmud, Sutra, Granth…</p><div class="rgTbl"><table><thead><tr><th>Book</th><th>Tradition</th><th>What it is</th><th>Read</th></tr></thead><tbody>'+rows.map(([r,b])=>'<tr><td><b>'+esc(b[0])+'</b></td><td>'+r.icon+' '+esc(r.name)+'</td><td>'+esc(b[1])+'</td><td>'+(b[2]&&/^https:\/\//.test(b[2])?'<a href="'+esc(b[2])+'" target="_blank" rel="noopener">Open ↗</a>':'—')+'</td></tr>').join('')+'</tbody></table></div>'; }
  else if(tab==='compare'){ const R=[['Followers',r=>r.people],['Share of the world',r=>r.share+'%'],['Began',r=>r.began],['Founder',r=>r.founder],['God',r=>r.god],['Main scripture',r=>r.books[0][0]],['Weekly day',r=>r.day],['Place of worship',r=>r.worship],['Holy cities',r=>r.city],['Main branches',r=>r.branches.slice(0,3).map(x=>x.split(/[,:]/)[0]).join(' · ')]];
   h='<p class="rgSub">The five side by side. Scroll sideways on a phone.</p><div class="rgTbl"><table><thead><tr><th></th>'+BIG.map(r=>'<th>'+r.icon+' '+esc(r.name)+'</th>').join('')+'</tr></thead><tbody>'+R.map(([k,f])=>'<tr><th>'+esc(k)+'</th>'+BIG.map(r=>'<td>'+esc(f(r))+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>'; }
  else if(tab==='days'){ const L=HOLY.filter(x=>x[0]===+mon); h='<p class="rgSub">Holy days that usually fall in '+MONTHS[mon-1]+'. Many follow the moon, so they move from year to year: check a calendar for this year’s exact date.</p><div class="rgGrid">'+L.map(x=>'<div class="rgCard"><div class="rgIco">'+x[1]+'</div><h3>'+esc(x[2])+'</h3><p>'+esc(x[3])+'</p></div>').join('')+'</div>'; }
  else if(tab==='quiz'){ const Q=QUIZ[qi%QUIZ.length]; const order=[0,1,2,3].sort((a,b)=>((a*7+qi*3)%4)-((b*7+qi*3)%4));
   h='<div class="rgCard rgQ"><p class="rgNote">Question '+(qi%QUIZ.length+1)+' of '+QUIZ.length+' · score '+qs+' of '+qa+'</p><h3>'+esc(Q[0])+'</h3>'+order.map(i=>'<button type="button" class="opt" data-rg="ans" data-i="'+i+'" data-noul>'+esc(Q[1][i])+'</button>').join('')+'<div class="rgRow"><button type="button" data-rg="next" data-noul>⏭ Next question</button><button type="button" data-rg="restart" data-noul>↺ Start over</button></div></div>'; }
  else if(tab==='ask'){ h='<div class="rgCard"><h3>🤖 Ask about any religion</h3><p class="rgNote">The answer comes from the AI and describes each faith the way it describes itself. It does not judge any faith true or false.</p><textarea id="rgAsk" placeholder="For example: What is the difference between Sunni and Shia Islam? What does the Bhagavad Gita teach about duty?"></textarea><div class="rgRow"><button type="button" data-rg="aiGo" data-noul>Ask</button><button type="button" data-rg="aiStop" data-noul>⏹ Stop</button><button type="button" data-rg="aiRead" data-noul>🔊 Read the answer</button></div><div class="rgAns" id="rgAns"></div>'+(sample?'':'<p class="rgNote">The AI answers inside claude.ai. Here, open the 🤖 AI screen from the Menu.</p>')+'</div>'; }
  B.innerHTML=h; if(tab==='ask'){ const a=$('rgAns'); if(a) a.textContent=aiAns; } }
 function paint(){ const d=box(); const T=[['big','⭐ The big five'],['all','🌍 Every tradition'],['shelf','📚 Scripture shelf'],['compare','⚖️ Compare'],['days','📅 Holy days'],['quiz','❓ Quiz'],['ask','🤖 Ask AI']];
  const regs=['all','Worldwide','Middle East','South Asia','East Asia','Africa','Americas','Europe'];
  d.innerHTML='<div class="kBar" data-sc="kRelig"><button type="button" data-ka="close" data-rg="close" aria-label="Close">✕</button></div><div class="rgIn"><div class="rgBrand">The Omni-Compass LLC · Omni-Galaxy Multi-Media Studios’ KAN-IN™ · Cultures & Religion</div><h2>✝️ ☪️ 🕉️ ☸️ ✡️ Cultures & Religion</h2><p class="rgSub">'+ALL.length+' traditions and '+ALL.reduce((n,r)=>n+(r.books||[]).length,0)+' scriptures and books. Each faith is described the way it describes itself; numbers from the Pew Research Center (2020 figures), smaller groups marked as estimates.</p>'+
   '<div class="rgTabs" role="tablist">'+T.map(([k,t])=>'<button type="button" data-rg="tab" data-t="'+k+'" aria-pressed="'+(tab===k)+'" data-noul>'+t+'</button>').join('')+'</div>'+
   '<div class="rgCtl"><input type="search" data-rg="q" aria-label="Search religions and scriptures" placeholder="🔎 Search: a faith, a book, a place…" value="'+esc(q)+'">'+
   '<select data-rg="pick" aria-label="Tradition" data-nodice><option value="">Every tradition</option>'+ALL.map(r=>'<option value="'+r.id+'"'+(pick===r.id?' selected':'')+'>'+r.icon+' '+esc(r.name)+'</option>').join('')+'</select>'+
   '<select data-rg="sort" aria-label="Order" data-nodice>'+[['size','Largest first'],['age','Oldest first'],['az','A to Z'],['region','By region'],['books','Most books first']].map(([v,t])=>'<option value="'+v+'"'+(sort===v?' selected':'')+'>'+t+'</option>').join('')+'</select>'+
   '<select data-rg="reg" aria-label="Region" data-nodice>'+regs.map(v=>'<option value="'+v+'"'+(reg===v?' selected':'')+'>'+(v==='all'?'Every region':v)+'</option>').join('')+'</select>'+
   (tab==='days'?'<select data-rg="mon" aria-label="Month" data-nodice>'+MONTHS.map((m,i)=>'<option value="'+(i+1)+'"'+(+mon===i+1?' selected':'')+'>'+m+'</option>').join('')+'</select>':'')+
   '</div><div id="rgBody"></div><p class="rgNote" style="margin-top:16px">Figures: Pew Research Center, “How the Global Religious Landscape Changed From 2010 to 2020” (2025). Reading links open public sites in a new tab. © 2026 The Omni-Compass LLC. All rights reserved.</p></div>';
  paintBody(); }
 const textOf=id=>{ const r=byId(id); if(!r) return ''; return r.name+'. '+(r.people?r.people+'. ':'')+(r.sum||'')+' Scriptures: '+(r.books||[]).map(b=>b[0]+': '+b[1]).join(' ')+(r.days?' Holy days: '+r.days.join('; ')+'.':''); };
 function speak(t){ try{ speechSynthesis.cancel(); const u=new SpeechSynthesisUtterance(t); try{ const v=window.KVOICE&&KVOICE('en'); if(v) u.voice=v; }catch(_){ } speechSynthesis.speak(u); }catch(_){ say('Read-aloud is not available on this device.'); } }
 async function ask(text){ if(!sample){ try{ close(); KAI.open(text); }catch(_){ } return; } if(busy) try{ busy.abort(); }catch(_){ } busy=new AbortController(); aiAns='Thinking…'; const a=$('rgAns'); if(a) a.textContent=aiAns;
  const prompt='You answer questions about world religions inside a family-friendly multimedia app. Describe each faith accurately and respectfully, the way its own followers and mainstream scholars describe it. Never rank religions or call one true or false. Name scriptures with chapter and verse where useful. Keep it under 250 words, plain language, no markdown headings.\n\nQuestion: '+text;
  try{ const r=await sample(prompt,{signal:busy.signal,cache:false,onText:({text:t})=>{ aiAns=t; const el=$('rgAns'); if(el) el.textContent=t; }}); aiAns=(r&&r.text)||aiAns; const el=$('rgAns'); if(el) el.textContent=aiAns; }
  catch(e){ if(e&&e.name==='AbortError') return; aiAns=e&&e.code==='rate_limited'?'The AI is busy right now. Try again in a minute.':e&&e.code==='not_granted'?'The AI is switched off for this page.':'The AI could not answer just now. Try again.'; const el=$('rgAns'); if(el) el.textContent=aiAns; } finally{ busy=null; } }
 async function onClick(e){ const b=e.target.closest('[data-rg]'); if(!b) return; const k=b.dataset.rg;
  if(k==='close') return close();
  if(k==='tab'){ tab=b.dataset.t; putLS('kanin-relig-tab',tab); return paint(); }
  if(k==='stop'){ try{ speechSynthesis.cancel(); }catch(_){ } return; }
  if(k==='read') return speak(textOf(b.dataset.id));
  if(k==='copy'){ const t=textOf(b.dataset.id); try{ await navigator.clipboard.writeText(t); say('📋 Copied.'); }catch(_){ say('Copy was blocked here: select the text and copy it by hand.'); } return; }
  if(k==='save'){ const r=byId(b.dataset.id); try{ await KLIB.save({kind:'file',name:'Religion · '+r.name,blob:new Blob([textOf(r.id)+'\n\nSource: Pew Research Center (2020 figures) and the tradition’s own texts.\n'],{type:'text/plain'}),meta:{from:'religions'}}); say('📁 Saved to your Projects: Religion · '+r.name+'.'); }catch(_){ say('This card could not be saved on this device.'); } return; }
  if(k==='ask'){ const r=byId(b.dataset.id); tab='ask'; paint(); const t=$('rgAsk'); const qq='Tell me about '+r.name+': its main beliefs, its scriptures and how its followers worship.'; if(t) t.value=qq; return ask(qq); }
  if(k==='aiGo'){ const t=$('rgAsk'); const v=t&&t.value.trim(); if(!v) return say('Type a question first.'); return ask(v); }
  if(k==='aiStop'){ if(busy) try{ busy.abort(); }catch(_){ } try{ speechSynthesis.cancel(); }catch(_){ } return; }
  if(k==='aiRead'){ if(aiAns) speak(aiAns); return; }
  if(k==='ans'){ const Q=QUIZ[qi%QUIZ.length]; const i=+b.dataset.i; if(b.parentElement.querySelector('.ok,.no')) return; qa++; if(i===Q[2]){ qs++; b.classList.add('ok'); say('✅ Right.'); } else { b.classList.add('no'); const right=b.parentElement.querySelector('[data-i="'+Q[2]+'"]'); if(right) right.classList.add('ok'); say('The answer: '+Q[1][Q[2]]+'.'); } const s=b.parentElement.querySelector('.rgNote'); if(s) s.textContent='Question '+(qi%QUIZ.length+1)+' of '+QUIZ.length+' · score '+qs+' of '+qa; return; }
  if(k==='next'){ qi++; return paintBody(); }
  if(k==='restart'){ qi=0; qs=0; qa=0; return paintBody(); } }
 function onChange(e){ const k=e.target.dataset.rg; if(!k) return; e.stopPropagation(); const v=e.target.value;
  if(k==='pick'){ pick=v; putLS('kanin-relig-pick',pick); } if(k==='sort'){ sort=v; putLS('kanin-relig-sort',sort); } if(k==='reg'){ reg=v; putLS('kanin-relig-reg',reg); } if(k==='mon'){ mon=+v; putLS('kanin-relig-mon',mon); } paintBody(); }
 function open(which){ const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||function(){})(); }catch(_){ }
  if(typeof which==='string'){ if(byId(which)){ pick=which; tab=BIG.some(r=>r.id===which)?'big':'all'; } else if(['big','all','shelf','compare','days','quiz','ask'].includes(which)) tab=which; }
  d.hidden=false; d.scrollTop=0; paint(); }
 function close(){ const d=$('kRelig'); if(d) d.hidden=true; try{ speechSynthesis.cancel(); }catch(_){ } if(busy) try{ busy.abort(); }catch(_){ } }
 document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&$('kRelig')&&!$('kRelig').hidden) close(); });
 try{ const gh=window.GOHOME; if(gh&&!gh.__krg){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__krg=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(!e.target.closest) return; if(e.target.closest('#kdHome,#lpMenu')) return close(); const r=e.target.closest('#rDock button'); if(r&&$('kRelig')&&!$('kRelig').hidden) close(); },true);
 /* Find: every tradition and every book can be found by name */
 (window.KFINDX=window.KFINDX||[]).push(add=>{ ALL.forEach(r=>{ add('Cultures & Religion',r.icon,r.name,'Religion · '+(r.people||''),()=>open(r.id)); (r.books||[]).forEach(b=>add('Cultures & Religion','📖',b[0],r.name+' · scripture',()=>{ open(r.id); }) ); }); });
 window.KRELIG={open,close,get count(){ return ALL.length; },get books(){ return ALL.reduce((n,r)=>n+(r.books||[]).length,0); },ALL,BIG};
})();
