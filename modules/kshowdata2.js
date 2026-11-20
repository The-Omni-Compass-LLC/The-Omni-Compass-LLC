(()=>{ /* 📺 KAN-IN SHOW BANK, volume 2 (v221): more questions, puzzles, price tags, KAN-IN panel surveys (invented panel), dates,
   clue words, pyramid categories, fill-in-the-blanks and public-domain tunes, added to volume 1. */
 const S=window.KSHOWDATA; if(!S) return; const T=(txt,cat)=>txt.split('\n').filter(Boolean).map(l=>{ const p=l.split('|'); return {q:p[0],a:p[1],w:[p[2],p[3],p[4]],lv:+p[5],cat:p[6]||cat}; });
 const add=(k,arr)=>{ S[k]=(S[k]||[]).concat(arr); };
 add('trivia',T(`What pumps blood around the body?|The heart|The lungs|The liver|The kidneys|1
How many teeth does a typical adult have, counting wisdom teeth?|32|28|30|36|2
What is the longest bone in the human body?|The femur (thigh bone)|The tibia|The humerus|The spine|2
What is the smallest bone in the human body?|The stapes, in the ear|A toe bone|The hyoid|A finger bone|3
Which organs filter the blood to make urine?|The kidneys|The liver|The spleen|The pancreas|2
What do red blood cells carry around the body?|Oxygen|Sugar|Hormones|Antibodies|2
Which vitamin does the skin make in sunlight?|Vitamin D|Vitamin C|Vitamin A|Vitamin B12|2
How many chambers does the human heart have?|4|2|3|6|2
What is the colored part of the eye called?|The iris|The pupil|The retina|The cornea|2
Which part of the brain mainly handles balance and coordination?|The cerebellum|The cerebrum|The brainstem|The hippocampus|4
What is the hardest substance in the human body?|Tooth enamel|Bone|Cartilage|Fingernail|3
About how many times does a resting adult heart beat each minute?|60 to 100|20 to 40|120 to 160|200 to 240|2
What tube carries food from the mouth to the stomach?|The esophagus|The trachea|The colon|The aorta|3
Which organ is the body’s largest internal organ?|The liver|The heart|The stomach|The lungs|3`,'Human Body'));
 add('trivia',T(`Who received the 1876 patent for the telephone?|Alexander Graham Bell|Thomas Edison|Nikola Tesla|Samuel Morse|2
Who built Europe’s first movable-type printing press?|Johannes Gutenberg|Leonardo da Vinci|Isaac Newton|Benjamin Franklin|3
Who announced the first successful polio vaccine in 1955?|Jonas Salk|Louis Pasteur|Edward Jenner|Alexander Fleming|3
Who created the dot-and-dash code used on telegraphs?|Samuel Morse|Alexander Graham Bell|Guglielmo Marconi|Thomas Edison|2
Who developed the theory of relativity?|Albert Einstein|Isaac Newton|Stephen Hawking|Niels Bohr|1
Which American flew a kite in a thunderstorm to study electricity?|Benjamin Franklin|Thomas Edison|Nikola Tesla|Michael Faraday|2
Edward Jenner made the first vaccine against which disease?|Smallpox|Polio|Measles|Rabies|3
Who made the practical light bulb of 1879 famous?|Thomas Edison|Nikola Tesla|Alexander Graham Bell|James Watt|2
Whose improvements to the steam engine powered the Industrial Revolution?|James Watt|George Stephenson|Henry Ford|Eli Whitney|4
Who introduced the moving assembly line for cars in 1913?|Henry Ford|Karl Benz|Ransom Olds|Walter Chrysler|3
Which Italian inventor pioneered long-distance radio?|Guglielmo Marconi|Alessandro Volta|Galileo Galilei|Enrico Fermi|3
Alessandro Volta invented an early form of what?|The electric battery|The radio|The telescope|The thermometer|3
What did Karl Benz build in 1885–86, often called the first true automobile?|A gasoline-powered car|A steam train|A bicycle|A motorcycle|4`,'Inventions'));
 add('trivia',T(`Who is the king of the gods in Greek mythology?|Zeus|Poseidon|Hades|Apollo|1
Who is the Greek god of the sea?|Poseidon|Zeus|Ares|Hermes|1
In Norse mythology, what is Thor’s hammer called?|Mjölnir|Gungnir|Excalibur|Gram|3
Which Greek hero had one weak spot, his heel?|Achilles|Hercules|Odysseus|Perseus|2
Who is the Roman counterpart of Zeus?|Jupiter|Mars|Neptune|Mercury|3
Which monster of Greek myth had snakes for hair?|Medusa|The Minotaur|The Sphinx|The Hydra|1
Which Egyptian god is shown with the head of a jackal?|Anubis|Ra|Horus|Osiris|3
Who flew too close to the sun on wings of wax and feathers?|Icarus|Daedalus|Perseus|Jason|2
What half-man, half-bull monster lived in the labyrinth on Crete?|The Minotaur|A centaur|A cyclops|The Chimera|2
Who is the Norse god of mischief?|Loki|Odin|Baldur|Freyr|2
Which Greek goddess is the goddess of wisdom?|Athena|Aphrodite|Hera|Artemis|2
In Greek myth, who opened the jar that let troubles into the world?|Pandora|Persephone|Helen|Medea|2`,'Mythology'));
 add('trivia',T(`What is the deepest known point in the ocean?|The Challenger Deep|The Puerto Rico Trench|The Java Trench|The Tonga Trench|3
What is the largest fish in the world?|The whale shark|The great white shark|The blue whale|The giant manta ray|2
What do we call the daily rise and fall of the sea?|Tides|Currents|Swells|Waves|1
About how much of Earth’s surface is ocean?|About 71%|About 50%|About 85%|About 60%|2
What is the largest coral reef system on Earth?|The Great Barrier Reef|The Belize Barrier Reef|The Red Sea reefs|The Florida Reef|1
Which sea animal has eight arms and can change color?|The octopus|The squid|The jellyfish|The starfish|1
What is a baby whale called?|A calf|A pup|A cub|A kid|2
Which ocean lies between Africa and Australia?|The Indian Ocean|The Atlantic Ocean|The Pacific Ocean|The Arctic Ocean|2
Why do swimmers float so easily in the Dead Sea?|Its water is extremely salty|Its water is warm|Its currents push up|It is very shallow|2`,'Ocean'));
 add('trivia',T(`What instrument measures air pressure?|A barometer|A thermometer|An anemometer|A hygrometer|2
What instrument measures wind speed?|An anemometer|A barometer|A seismometer|A thermometer|3
What is an Atlantic tropical storm with winds of 74 mph or more called?|A hurricane|A tornado|A monsoon|A blizzard|1
What are hurricane-strength storms called in the western Pacific?|Typhoons|Tornadoes|Blizzards|Monsoons|3
Which scale rates tornadoes in the United States today?|The Enhanced Fujita scale|The Richter scale|The Saffir–Simpson scale|The Beaufort scale|4
What causes the sound of thunder?|Air heated by lightning expanding fast|Clouds bumping together|Rain hitting the ground|Wind in the trees|2
What are balls of ice that fall from thunderstorms called?|Hail|Sleet|Snow|Frost|1
On which temperature scale does water freeze at 32 degrees?|Fahrenheit|Celsius|Kelvin|Centigrade|1`,'Weather'));
 add('trivia',T(`What is the official language of Brazil?|Portuguese|Spanish|French|English|1
In which country is the city of Marrakech?|Morocco|Egypt|Tunisia|Algeria|2
What is the currency of Japan?|The yen|The yuan|The won|The baht|1
What is the currency of the United Kingdom?|The pound sterling|The euro|The dollar|The franc|1
Which country gave the Statue of Liberty to the United States?|France|England|Spain|Italy|1
Where did the ancient Olympic Games begin?|Greece|Italy|Egypt|Turkey|1
How do you say “thank you” in Japanese?|Arigatō|Konnichiwa|Sayōnara|Sumimasen|2
Which language has the most native speakers?|Mandarin Chinese|English|Spanish|Hindi|2
Which country is called the Land of the Rising Sun?|Japan|China|Thailand|South Korea|1
The tango dance comes from which country?|Argentina|Spain|Brazil|Cuba|2
In which country is the ancient rock city of Petra?|Jordan|Egypt|Israel|Turkey|3
Which spring festival of colors is celebrated in India?|Holi|Diwali|Eid|Pongal|2`,'World Cultures'));
 add('trivia',T(`How many days are in a week?|7|5|6|10|1
What color do you get when you mix blue and yellow?|Green|Purple|Orange|Brown|1
What color do you get when you mix red and white?|Pink|Purple|Orange|Gray|1
How many legs does an insect have?|6|8|4|10|1
Which animal says “moo”?|A cow|A sheep|A pig|A goat|1
What shape has three sides?|A triangle|A square|A circle|A pentagon|1
How many months are in a year?|12|10|11|13|1
What do bees make?|Honey|Milk|Silk|Butter|1
Which season comes after winter?|Spring|Summer|Autumn|Fall|1
How many wheels does a bicycle have?|2|3|4|1|1
What color is a ripe banana?|Yellow|Blue|Purple|Red|1
Which planet do we live on?|Earth|Mars|Venus|Jupiter|1
What is 10 + 10?|20|15|25|100|1
Which animal is called the king of the jungle?|The lion|The elephant|The tiger|The gorilla|1
What do caterpillars turn into?|Butterflies or moths|Beetles|Bees|Spiders|1
What do you call frozen water?|Ice|Steam|Fog|Dew|1`,'Kids'));
 add('trivia',T(`What is the golden statuette of the Academy Awards called?|Oscar|Emmy|Tony|Grammy|1
Which award honors excellence in television?|The Emmy|The Oscar|The Tony|The Grammy|2
Which award honors Broadway theater?|The Tony|The Emmy|The Oscar|The Golden Globe|2
In what city is the Hollywood film district?|Los Angeles|New York|Chicago|San Francisco|1
What was Walt Disney’s first feature-length animated film, in 1937?|Snow White and the Seven Dwarfs|Pinocchio|Cinderella|Bambi|3
What is the list of names shown at the end of a film called?|The credits|The trailer|The script|The reel|1
What is a short preview of a coming film called?|A trailer|A sequel|A cameo|A montage|1
When a film director calls “cut!”, what happens?|Filming stops|Filming starts|The scene changes|The actors bow|1
What is a film that continues an earlier story called?|A sequel|A prequel|A remake|A spin-off|1
Which country’s film industry is nicknamed Bollywood?|India|Nigeria|Bangladesh|Pakistan|2
Charlie Chaplin was a famous star of which era?|Silent films|Color musicals|TV sitcoms|Video games|2`,'Movies & TV'));
 add('trivia',T(`Which company makes the PlayStation consoles?|Sony|Nintendo|Microsoft|Sega|1
Which company makes the Xbox consoles?|Microsoft|Sony|Nintendo|Apple|1
What does Wi-Fi let devices do?|Join a network without wires|Charge without cables|Print documents|Store files offline|1
What does HTML stand for?|HyperText Markup Language|High Tech Modern Language|Home Tool Markup Language|Hyperlink Text Management Language|3
In computer storage, what does GB stand for?|Gigabyte|Gigabit box|Great byte|Gram byte|1
What was Atari’s 1972 arcade game of table tennis called?|Pong|Tennis Pro|Paddle Ball|Ping|3
What kind of software protects a computer from harmful programs?|Antivirus software|A spreadsheet|A web browser|A compiler|1
What is a small picture you click to open a program called?|An icon|A cursor|A pixel|A widget bar|1`,'Tech'));
 add('trivia',T(`What does ATM stand for?|Automated teller machine|Automatic transfer money|All-time maximum|Account transfer method|2
What do you call a person who starts a business?|An entrepreneur|An accountant|A landlord|A banker|1
What does “profit” mean?|Money left after costs are paid|All the money taken in|Money borrowed|Money owed in tax|1
What is the central bank system of the United States called?|The Federal Reserve|The Treasury|Wall Street|The Mint|3
On a stock market, what is a “bull market”?|A rising market|A falling market|A closed market|A foreign market|3
What currency do most European Union countries use?|The euro|The pound|The franc|The mark|1`,'Money'));
 add('trivia',T(`How many wheels does a typical car have, not counting the spare?|4|3|6|8|1
What is Japan’s high-speed train network called?|The Shinkansen|The TGV|The Eurostar|The Maglev Express|3
In which country does the TGV high-speed train run?|France|Germany|Italy|Spain|3
What does a car’s speedometer show?|Its speed|Its fuel|Its engine heat|The time|1
Which 1825 English line was the first public railway to use steam locomotives?|The Stockton and Darlington Railway|The London Underground|The Orient Express|The Liverpool Overhead|5`,'Transport'));
 add('trivia',T(`Which planet has the Great Red Spot?|Jupiter|Mars|Saturn|Neptune|2|Space
What was NASA’s program that landed people on the Moon?|Apollo|Gemini|Mercury|Voyager|2|Space
What does a light-year measure?|Distance|Time|Brightness|Speed|2|Space
What is the larger of Mars’s two moons?|Phobos|Deimos|Titan|Europa|4|Space
What is Saturn’s largest moon?|Titan|Europa|Ganymede|Io|3|Space
Ganymede, the largest moon in the solar system, orbits which planet?|Jupiter|Saturn|Neptune|Uranus|4|Space
Who became the first human in space in 1961?|Yuri Gagarin|Neil Armstrong|Alan Shepard|John Glenn|2|Space
What kind of star is the Sun?|A yellow dwarf|A red giant|A white dwarf|A neutron star|3|Space
What is the chemical symbol for iron?|Fe|Ir|In|I|2|Science
What is the chemical formula for table salt?|NaCl|KCl|NaOH|CaCO₃|3|Science
What kind of energy does a moving object have?|Kinetic energy|Potential energy|Chemical energy|Nuclear energy|2|Science
Which particle carries a negative charge?|The electron|The proton|The neutron|The nucleus|2|Science
Which gas makes up most of the Sun?|Hydrogen|Helium|Oxygen|Carbon|3|Science
Which metal is liquid at room temperature?|Mercury|Lead|Tin|Aluminum|2|Science
What is the study of living things called?|Biology|Geology|Chemistry|Physics|1|Science
What do you call an animal that eats only plants?|A herbivore|A carnivore|An omnivore|A predator|1|Science
What is the capital of Italy?|Rome|Milan|Venice|Naples|1|Geography
What is the capital of Spain?|Madrid|Barcelona|Seville|Valencia|1|Geography
What is the capital of Germany?|Berlin|Munich|Frankfurt|Hamburg|1|Geography
What is the capital of Kenya?|Nairobi|Mombasa|Kampala|Addis Ababa|3|Geography
What is the capital of Argentina?|Buenos Aires|Santiago|Lima|Montevideo|2|Geography
What is the capital of South Korea?|Seoul|Busan|Incheon|Daegu|2|Geography
What is the highest mountain in Africa?|Mount Kilimanjaro|Mount Kenya|Mount Elgon|Mount Toubkal|2|Geography
What is the largest country in the world by area?|Russia|Canada|China|United States|1|Geography
What is the largest island that is not a continent?|Greenland|New Guinea|Borneo|Madagascar|2|Geography
Which US state is nicknamed the Sunshine State?|Florida|California|Arizona|Hawaii|1|Geography
What is the capital of India?|New Delhi|Mumbai|Kolkata|Bangalore|2|Geography
Which mountain range runs down the west side of South America?|The Andes|The Rockies|The Alps|The Himalayas|2|Geography
What is the capital of Turkey?|Ankara|Istanbul|Izmir|Antalya|3|Geography
Which two countries share the world’s longest international border?|Canada and the United States|Russia and China|Argentina and Chile|Russia and Kazakhstan|3|Geography
Which wall was built across northern China over many centuries?|The Great Wall|Hadrian’s Wall|The Berlin Wall|The Western Wall|1|History
Who was the first emperor of Rome?|Augustus|Julius Caesar|Nero|Caligula|3|History
Which ancient wonder stood at Alexandria in Egypt?|The Lighthouse (Pharos)|The Hanging Gardens|The Colossus|The Temple of Artemis|4|History
Which queen of Egypt allied with Julius Caesar and Mark Antony?|Cleopatra|Nefertiti|Hatshepsut|Nefertari|2|History
In what year did the American Civil War end?|1865|1861|1870|1855|3|History
Who gave the “I Have a Dream” speech in 1963?|Martin Luther King Jr.|Malcolm X|John F. Kennedy|Rosa Parks|1|History
In which country did the Renaissance begin?|Italy|France|England|Spain|2|History
Who led India’s nonviolent movement for independence?|Mahatma Gandhi|Jawaharlal Nehru|Indira Gandhi|Muhammad Ali Jinnah|2|History
Which ship carried the Pilgrims to America in 1620?|The Mayflower|The Santa María|The Endeavour|The Victory|1|History
Which civilization built Chichén Itzá in Mexico?|The Maya|The Aztec|The Inca|The Olmec|3|History
Who was the first woman to fly solo across the Atlantic, in 1932?|Amelia Earhart|Bessie Coleman|Harriet Quimby|Sally Ride|2|History
How many players does a volleyball team have on the court?|6|5|7|9|2|Sports
In bowling, what is knocking down all ten pins with the first ball?|A strike|A spare|A split|A turkey|1|Sports
In which sport do players hit a shuttlecock?|Badminton|Tennis|Squash|Table tennis|1|Sports
How many points is a basket from beyond the arc worth in basketball?|3|2|4|1|1|Sports
Which country has won the most men’s FIFA World Cups?|Brazil|Germany|Italy|Argentina|2|Sports
In golf, what is one stroke under par on a hole?|A birdie|An eagle|A bogey|An albatross|2|Sports
How many players does an ice hockey team have on the ice, goalie included?|6|5|7|11|2|Sports
Which martial art’s name means “the gentle way”?|Judo|Karate|Taekwondo|Kung fu|4|Sports
How long is an Olympic swimming pool?|50 meters|25 meters|100 meters|75 meters|2|Sports
How many strings does a standard violin have?|4|5|6|3|2|Music
What is the highest female singing voice?|Soprano|Alto|Tenor|Mezzo-soprano|2|Music
What is the lowest standard male singing voice?|Bass|Baritone|Tenor|Alto|2|Music
Which composer kept composing after losing his hearing?|Ludwig van Beethoven|Johann Sebastian Bach|Franz Schubert|Antonio Vivaldi|2|Music
What is a group of three musicians called?|A trio|A duet|A quartet|A sextet|1|Music
Which instrument family does the trumpet belong to?|Brass|Woodwinds|Strings|Percussion|1|Music
What does “piano” mean as a direction in music?|Soft|Loud|Fast|Slow|2|Music
What is the symbol at the start of a staff, like the G or F symbol, called?|A clef|A rest|A tie|A slur|2|Music
Which country is most famous for the bagpipe tradition?|Scotland|Ireland|Wales|Norway|1|Music
What is the main ingredient of traditional pesto?|Basil|Spinach|Parsley|Mint|2|Food
What is sushi rice seasoned with?|Rice vinegar|Soy sauce|Lime juice|Fish sauce|3|Food
Which fruit wears its seeds on the outside?|The strawberry|The raspberry|The blueberry|The kiwi|1|Food
Which vegetable is fermented to make sauerkraut?|Cabbage|Cucumber|Carrot|Turnip|2|Food
What is miso mainly made from?|Fermented soybeans|Rice flour|Seaweed|Fish|3|Food
What kind of food is Gouda?|Cheese|Bread|Sausage|Wine|1|Food
Besides corn, what grain are tortillas commonly made from?|Wheat|Rice|Barley|Oats|2|Food
Which country is pad thai from?|Thailand|Vietnam|China|Malaysia|1|Food
Falafel is made mainly from what?|Chickpeas or fava beans|Lentils|Potatoes|Rice|2|Food
How many legs does a lobster have, counting the claws?|10|8|6|12|4|Animals
What is the largest land animal?|The African elephant|The rhinoceros|The giraffe|The hippopotamus|1|Animals
What is a group of wolves called?|A pack|A pride|A herd|A flock|1|Animals
Which bird fans out a huge, colorful tail?|The peacock|The flamingo|The parrot|The swan|1|Animals
On which continent do giraffes live in the wild?|Africa|Asia|South America|Australia|2|Animals
Which mammal lays eggs?|The platypus|The kangaroo|The koala|The opossum|3|Animals
What word describes an animal that is active at night?|Nocturnal|Diurnal|Migratory|Dormant|2|Animals
How many arms does a starfish usually have?|5|4|6|8|1|Animals
What is a group of fish swimming together called?|A school|A pack|A herd|A colony|1|Animals
Which animal stands beside the emu on Australia’s coat of arms?|The kangaroo|The koala|The wombat|The platypus|2|Animals
What is a word that means the opposite of another word?|An antonym|A synonym|A homophone|A pronoun|1|Words
Which word is spelled correctly?|Necessary|Neccessary|Necesary|Neccesary|2|Words
What is the past tense of “run”?|Ran|Runned|Running|Runs|1|Words
Which punctuation mark ends a question?|A question mark|A period|A comma|A colon|1|Words
What is the plural of “child”?|Children|Childs|Childes|Childrens|1|Words
Which of these is a verb?|Jump|Happy|Blue|Table|1|Words
What do “there,” “their” and “they’re” have in common?|They sound the same|They mean the same|They are all verbs|They are all nouns|2|Words
What is 12 × 12?|144|124|132|154|1|Math
What is half of 90?|45|40|50|35|1|Math
How many sides does an octagon have?|8|6|10|7|1|Math
What is 25% of 80?|20|25|16|40|2|Math
What is the perimeter of a square with sides of 5?|20|25|10|15|2|Math
What is 9 squared?|81|18|72|99|1|Math
How many minutes are in three hours?|180|120|300|360|1|Math
What comes next: 2, 4, 8, 16…?|32|24|20|30|2|Math
How many degrees are in a full circle?|360|180|90|400|1|Math
Who wrote “Hamlet”?|William Shakespeare|Christopher Marlowe|John Milton|Ben Jonson|1|Books & Art
Who wrote “Alice’s Adventures in Wonderland”?|Lewis Carroll|J. M. Barrie|Kenneth Grahame|Beatrix Potter|2|Books & Art
Who painted the ceiling of the Sistine Chapel?|Michelangelo|Leonardo da Vinci|Raphael|Botticelli|2|Books & Art
Which Spanish artist co-founded Cubism?|Pablo Picasso|Salvador Dalí|Francisco Goya|Joan Miró|2|Books & Art
Who wrote “Little Women”?|Louisa May Alcott|Jane Austen|Emily Dickinson|Harriet Beecher Stowe|2|Books & Art
Who wrote “Frankenstein”?|Mary Shelley|Bram Stoker|Edgar Allan Poe|Charlotte Brontë|2|Books & Art
Who wrote “Dracula”?|Bram Stoker|Mary Shelley|Oscar Wilde|Robert Louis Stevenson|2|Books & Art
Who painted “The Persistence of Memory”, with its melting clocks?|Salvador Dalí|René Magritte|Pablo Picasso|Joan Miró|2|Books & Art
Who wrote “Treasure Island”?|Robert Louis Stevenson|Jules Verne|Daniel Defoe|Jack London|2|Books & Art
Who wrote “Twenty Thousand Leagues Under the Seas”?|Jules Verne|H. G. Wells|Arthur Conan Doyle|Mark Twain|2|Books & Art
Which fictional detective lived at 221B Baker Street?|Sherlock Holmes|Hercule Poirot|Miss Marple|Sam Spade|2|Books & Art
What is the tallest kind of tree in the world?|The coast redwood|The giant sequoia|The Douglas fir|The baobab|3|Nature
What is a scientist who studies plants called?|A botanist|A zoologist|An ecologist|A geologist|2|Nature
What kind of rock forms when lava or magma cools?|Igneous rock|Sedimentary rock|Metamorphic rock|Limestone|3|Nature
What is a baby frog called?|A tadpole|A kit|A cub|A fawn|1|Nature
What part of a plant takes in water from the soil?|The roots|The leaves|The flowers|The petals|1|Nature
What is water turning into vapor called?|Evaporation|Condensation|Precipitation|Freezing|1|Nature
On which date is Christmas Day celebrated in most Western countries?|December 25|December 24|January 6|December 31|1|Holidays
What is the Jewish New Year called?|Rosh Hashanah|Yom Kippur|Passover|Purim|3|Holidays
Which holiday ends the fasting month of Ramadan?|Eid al-Fitr|Eid al-Adha|Diwali|Nowruz|3|Holidays
What is the Persian New Year, held at the spring equinox, called?|Nowruz|Songkran|Tết|Holi|4|Holidays
Lunar New Year parades often feature what kind of dance?|A lion or dragon dance|A tango|A flamenco|A hula|2|Holidays
Which holiday falls on October 31?|Halloween|Thanksgiving|Easter|Labor Day|1|Holidays`));
 const P=(txt)=>txt.split('\n').filter(Boolean).map(l=>{ const p=l.split('|'); return {cat:p[0],ph:p[1]}; });
 add('phrases',P(`Phrase|A PENNY SAVED IS A PENNY EARNED
Phrase|ALL THAT GLITTERS IS NOT GOLD
Phrase|BIRDS OF A FEATHER FLOCK TOGETHER
Phrase|DON'T JUDGE A BOOK BY ITS COVER
Phrase|KNOWLEDGE IS POWER
Phrase|LAUGHTER IS THE BEST MEDICINE
Phrase|SLOW AND STEADY WINS THE RACE
Phrase|THE SKY IS THE LIMIT
Phrase|TWO HEADS ARE BETTER THAN ONE
Phrase|WHERE THERE'S A WILL THERE'S A WAY
Phrase|BETTER SAFE THAN SORRY
Phrase|GREAT MINDS THINK ALIKE
Thing|A JAR OF HOMEMADE JAM
Thing|POLKA DOT UMBRELLA
Thing|GLOW IN THE DARK STICKERS
Thing|ANTIQUE POCKET WATCH
Thing|WIRELESS HEADPHONES
Thing|A BASKET OF FRESH LAUNDRY
Thing|SNOW GLOBE
Thing|PAPER AIRPLANE
Place|THE EIFFEL TOWER
Place|A BUSY TRAIN STATION
Place|THE SAHARA AT SUNRISE
Place|AN ICE SKATING RINK
Place|A QUIET PUBLIC LIBRARY
Place|THE TOP OF A LIGHTHOUSE
Place|A BUSTLING NIGHT MARKET
Place|A RECORDING STUDIO
Food & Drink|BLUEBERRY MUFFINS
Food & Drink|HOT AND SOUR SOUP
Food & Drink|MANGO SMOOTHIE
Food & Drink|PEPPERONI PIZZA SLICE
Food & Drink|CINNAMON ROLLS
Food & Drink|CHICKEN TIKKA MASALA
Food & Drink|FRESH GUACAMOLE AND CHIPS
Food & Drink|APPLE PIE A LA MODE
Event|SCIENCE FAIR
Event|COOKING COMPETITION
Event|TALENT SHOW
Event|SURPRISE ANNIVERSARY DINNER
Event|NEIGHBORHOOD BLOCK PARTY
Event|MIDNIGHT MOVIE PREMIERE
Occupation|ASTRONAUT
Occupation|ZOOKEEPER
Occupation|GRAPHIC DESIGNER
Occupation|LIGHTHOUSE KEEPER
Occupation|SOUND ENGINEER
Occupation|PARK RANGER
Around the House|SPICE RACK
Around the House|COZY FLANNEL BLANKET
Around the House|GARAGE WORKBENCH
Around the House|LAUNDRY BASKET
Fun & Games|PILLOW FORT
Fun & Games|WATER BALLOON FIGHT
Fun & Games|MUSICAL CHAIRS
Fun & Games|TREASURE HUNT
Fun & Games|PAPER ROCK SCISSORS
On the Map|MOUNT EVEREST
On the Map|PACIFIC OCEAN
On the Map|AMAZON RIVER
On the Map|CAPE OF GOOD HOPE
On the Map|GRAND CANAL OF VENICE
Animal Kingdom|BOTTLENOSE DOLPHIN
Animal Kingdom|BALD EAGLE
Animal Kingdom|GIANT PANDA
Animal Kingdom|EMPEROR PENGUIN
Animal Kingdom|MONARCH BUTTERFLY
Animal Kingdom|SNOW LEOPARD
Science|SOLAR ECLIPSE
Science|LAWS OF GRAVITY
Science|PERIODIC TABLE OF ELEMENTS
Science|PHOTOSYNTHESIS
Science|SHOOTING STAR
Holiday|FOURTH OF JULY FIREWORKS
Holiday|NEW YEAR'S RESOLUTIONS
Holiday|THANKSGIVING TURKEY
Holiday|VALENTINE'S DAY CARDS
Holiday|HALLOWEEN COSTUME PARTY
Music|ROCK AND ROLL
Music|SYMPHONY ORCHESTRA
Music|DRUM SOLO
Music|SING ALONG
Music|ELECTRIC GUITAR`));
 add('prices',`A pack of 24 pencils|6.49|No. 2
A bag of tortilla chips|4.29|family size
A jar of salsa|3.79|16 ounces
A box of 12 granola bars|5.99|variety pack
A gallon of orange juice|7.49|not from concentrate
A bag of shredded cheese|3.99|8 ounces
A pound of ground coffee beans|11.99|medium roast
A bottle of dish soap|3.49|24 ounces
A 12-roll pack of paper towels|17.99|select-a-size
A box of trash bags|12.99|40 count
A rain jacket|49.99|lightweight
A pair of running shoes|89.99|mid-range
A backpack|39.99|school size
A water bottle|24.99|insulated, 24 ounces
A desk lamp|29.99|LED
A board game|24.99|family classic style
A jigsaw puzzle|17.99|1,000 pieces
A bag of potting soil|9.99|1 cubic foot
A garden hose|34.99|50 feet
A cordless drill|79.99|20 volt kit
A soccer ball|24.99|size 5
A skateboard|59.99|complete
A smart watch|199.99|fitness style
A tablet computer|329.99|10 inch
A robot vacuum|249.99|basic model
An electric toothbrush|49.99|rechargeable
An air fryer|89.99|5 quart
A carry-on suitcase|129.99|hard shell
A tank of propane for a grill|24.99|20 pound exchange
A movie night snack combo|18.50|large popcorn and two drinks`.split('\n').map(l=>{ const p=l.split('|'); return {it:p[0],v:+p[1],n:p[2]}; }));
 add('survey',`Name something people do at the gym|Lift weights:34:weights,weightlifting;Run on a treadmill:24:run,treadmill,cardio;Take a class:12:class,yoga,spin;Stretch:10:;Swim:10:pool;Take a selfie:10:selfie,photo
Name a reason a dog might bark|Someone at the door:36:doorbell,visitor,stranger;Wants food:18:hungry,food;Wants to go out:16:bathroom,outside;Sees another animal:14:cat,squirrel,dog;Scared:8:fear;Bored:8:play
Name something you might find in a junk drawer|Batteries:28:battery;Rubber bands:18:rubber band;Pens:16:pen,pencils;Keys:14:key;Tape:12:;Coupons:12:receipts
Name a famous sea creature from stories|Mermaid:30:mermaids;Sea monster:22:monster,kraken;Shark:18:;Whale:14:;Octopus:10:;Seahorse:6:
Name something people bring to a birthday party|A gift:52:gift,present;A card:18:;Balloons:10:balloon;Cake:10:;Flowers:6:;Party hat:4:hat
Name something that goes up and down|An elevator:32:elevator,lift;A seesaw:20:teeter totter;A yo-yo:16:yoyo;Stock prices:12:stocks,stock market;A roller coaster:12:coaster;The tide:8:tides
Name a sound you hear at night|Crickets:32:cricket,bugs;Snoring:20:snore;Dogs barking:16:dog,barking;Sirens:12:siren;Owls:10:owl;Wind:10:
Name something people lose a lot|Keys:42:key;Phone:22:;Glasses:12:sunglasses;Socks:10:sock;Remote control:8:remote;Wallet:6:
Name a job where you wear gloves|Doctor:28:surgeon,nurse;Chef:20:cook;Gardener:16:landscaper;Construction worker:14:builder;Firefighter:12:;Dentist:10:
Name something kids collect|Trading cards:30:cards,baseball cards;Stickers:22:sticker;Rocks:14:stones;Toys:14:figures,action figures;Coins:10:;Stuffed animals:10:plush,teddy bears
Name a popular sandwich|Peanut butter and jelly:30:pb&j,pbj,peanut butter;Ham and cheese:22:ham;Grilled cheese:18:;Turkey:14:;BLT:10:bacon;Tuna:6:
Name something you do before going to bed|Brush teeth:38:teeth,brush;Read:20:book;Take a shower:14:shower,bath;Set an alarm:12:alarm;Check phone:10:phone;Pray:6:prayers
Name a place people go on a first date|Restaurant:40:dinner;Movies:26:movie,cinema;Coffee shop:14:coffee,cafe;Park:10:;Bowling:6:;Mini golf:4:golf
Name something that is often red|Fire truck:30:firetruck;Apple:24:;Stop sign:16:;Rose:12:roses;Strawberry:10:;Lips:8:
Name a reason people wake up in the night|Bathroom:44:pee,toilet;Noise:16:sound;Bad dream:14:nightmare,dream;Thirsty:10:water;Baby crying:10:baby,kids;Too hot:6:hot
Name something you take on a camping trip|Tent:38:;Sleeping bag:22:;Flashlight:14:torch;Food:10:snacks,marshmallows;Bug spray:8:;Matches:8:lighter
Name a type of weather people complain about|Rain:32:rainy;Heat:24:hot,humidity;Snow:18:;Cold:14:;Wind:8:windy;Fog:4:
Name an animal with a long neck|Giraffe:66:;Swan:10:;Ostrich:8:;Flamingo:8:;Camel:4:llama;Dinosaur:4:brachiosaurus
Name something people do on their phone|Text:34:texting,message;Call:20:phone call,talk;Social media:18:scroll;Play games:12:games;Take photos:10:pictures,camera;Watch videos:6:videos
Name a dessert people order at a restaurant|Cheesecake:30:;Ice cream:24:;Chocolate cake:20:cake;Pie:12:apple pie;Brownie:8:sundae;Tiramisu:6:`.split('\n').map(l=>{ const [q,r]=l.split('|'); return {q,ans:r.split(';').map(x=>{ const [a,pts,al]=x.split(':'); return {a,pts:+pts,al:(al?al.split(','):[]).filter(Boolean)}; })}; }));
 add('years',`The Great Fire of London|1666
Isaac Newton publishes his laws of motion (the Principia)|1687
The Wright brothers’ first powered flight at Kitty Hawk|1903
The Treaty of Versailles is signed|1919
The first Academy Awards are presented|1929
The first transatlantic radio signal is received|1901
The first email is sent between computers on ARPANET|1971
The first commercial cell phone call is made|1973
The Hubble Space Telescope’s mirror is repaired by astronauts|1993
The Sydney Opera House opens|1973
The Statue of Liberty is dedicated|1886
The Brooklyn Bridge opens|1883
The Suez Canal opens|1869
The first Tour de France is raced|1903
The first FIFA World Cup is played|1930
The first Winter Olympic Games are held|1924
Apple releases the first Macintosh|1984
The Nintendo Entertainment System launches in North America|1985
The euro launches as an electronic currency|1999
The first Harry Potter book is published|1997
The Titanic is discovered on the ocean floor|1985
Neil Armstrong and Buzz Aldrin land on the Moon|1969
The Panama Canal is handed over to Panama|1999
The Eiffel Tower is opened at the World’s Fair|1889
Ludwig van Beethoven is born|1770
Wolfgang Amadeus Mozart is born|1756
Leonardo da Vinci is born|1452
The first public showing of a moving picture by the Lumière brothers|1895
Vaccination against smallpox is introduced by Edward Jenner|1796
The first successful heart transplant|1967
The Space Shuttle makes its first flight|1981
The International Space Station’s first crew arrives|2000
The Mars rover Curiosity lands|2012
The Rosetta probe’s lander touches down on a comet|2014
The first iPod is released|2001
The first text message is sent|1992
The DVD format is introduced in Japan|1996
The first Super Mario Bros. game is released|1985
Mount Fuji’s last eruption|1707
The US buys Alaska from Russia|1867`.split('\n').map(l=>{ const p=l.split('|'); return {ev:p[0],y:+p[1]}; }));
 add('clues',`GALAXY|spiral,Andromeda,stars,Milky,universe,cosmos
WATERFALL|Niagara,cascade,cliff,river,plunge,falls
KANGAROO|joey,pouch,hop,Australia,marsupial,roo
SAXOPHONE|reed,jazz,brass,sax,horn,blow
BLIZZARD|whiteout,snowstorm,wind,winter,snow,storm
HELICOPTER|rotor,hover,chopper,blades,fly,pilot
MERMAID|tail,fins,sea,legend,fish,ocean
POPCORN|kernel,butter,movie,pop,snack,corn
TORNADO|funnel,twister,Kansas,storm,spin,wind
VAMPIRE|fangs,Dracula,cape,bat,blood,coffin
ORCHESTRA|conductor,symphony,violins,musicians,concert,band
SKELETON|bones,skull,ribs,Halloween,body,spooky
ESCALATOR|steps,mall,moving,stairs,up,ride
ICEBERG|Titanic,tip,floating,glacier,ice,frozen
PARACHUTE|skydive,canopy,jump,plane,chute,fall
COMPASS|needle,north,navigate,direction,magnet,map
FIREWORKS|sparkle,boom,July,display,rocket,explode
RAINBOW|arc,prism,colors,rain,pot,spectrum
DINOSAUR|fossil,extinct,T-rex,Jurassic,reptile,bones
TREASURE|chest,gold,pirate,map,jewels,buried
ASTRONAUT|spacesuit,orbit,NASA,rocket,moon,space
CROWN|jewels,king,queen,royal,throne,head
SUBMARINE|periscope,sonar,underwater,navy,dive,sub
VOLLEYBALL|spike,net,beach,serve,ball,court
BAKERY|oven,bread,croissant,pastry,baker,shop
MICROPHONE|mic,sing,voice,stage,karaoke,speak
HAMMOCK|swing,relax,trees,porch,nap,hanging
ACCORDION|squeeze,bellows,polka,keys,instrument,fold
SNORKEL|mask,breathe,reef,tube,swim,dive
PUMPKIN|jack-o'-lantern,orange,pie,Halloween,carve,gourd
WIZARD|wand,spell,magic,beard,hat,sorcerer
LANTERN|lamp,light,candle,glow,camping,lamplight
CACTUS|spines,desert,succulent,prickly,dry,plant
PIANO|keys,grand,ivory,keyboard,pianist,instrument
GLACIER|ice,Alaska,melt,mountain,frozen,river
SANDCASTLE|bucket,beach,tower,shovel,sand,build
TRAMPOLINE|bounce,jump,springs,backyard,flip,mat
NEWSPAPER|headline,print,daily,news,paper,read
CAMPFIRE|marshmallows,logs,flames,smoke,camping,fire
ROLLERCOASTER|loop,thrill,ride,park,drop,coaster`.split('\n').map(l=>{ const [w,c]=l.split('|'); return {w,c:c.split(',')}; }));
 add('pyramid',`Things in a garage|CAR:you drive it to work;BICYCLE:two wheels and pedals;LADDER:you climb it to reach high places;TOOLBOX:it holds your hammer and wrench;LAWNMOWER:it cuts the grass;SHOVEL:you dig with it
Things at a birthday party|CAKE:you blow out the candles on it;BALLOONS:colorful and full of air;PRESENTS:wrapped gifts;CANDLES:you make a wish and blow them out;GAMES:party fun like musical chairs;SONG:everyone sings it to you
Things that are hot|SUN:the star at the center of our solar system;FIRE:flames from burning wood;OVEN:you bake bread in it;LAVA:melted rock from a volcano;COFFEE:a morning drink;DESERT:a dry, sandy place
Things in a toolbox|HAMMER:you hit nails with it;SCREWDRIVER:you turn screws with it;WRENCH:you tighten bolts with it;PLIERS:you grip and bend wire with them;TAPE:measuring or sticky;LEVEL:shows if a shelf is straight
Things in the sky|CLOUD:white and fluffy;MOON:it shines at night;RAINBOW:colors after the rain;BIRD:it flies and sings;KITE:you fly it on a string;PLANE:it carries passengers far away
Musical instruments|GUITAR:six strings you strum;DRUMS:you hit them with sticks;PIANO:black and white keys;VIOLIN:you play it with a bow;FLUTE:you blow across it;TRUMPET:a brass horn with valves
Farm animals|COW:it gives milk;PIG:it rolls in the mud;HORSE:you ride it;SHEEP:it gives wool;CHICKEN:it lays eggs;GOAT:it eats almost anything
Things you wear in winter|SCARF:you wrap it around your neck;GLOVES:they keep your hands warm;BOOTS:tall shoes for snow;COAT:a heavy jacket;HAT:it keeps your head warm;MITTENS:gloves without fingers
Things that are yellow|BANANA:a long fruit you peel;LEMON:a sour fruit;SUN:it lights the day;CHEESE:made from milk;CORN:you eat it on the cob;TAXI:a car you hail in the city
Things at the zoo|LION:king of the jungle;ELEPHANT:it has a trunk;MONKEY:it swings from trees;ZEBRA:black and white stripes;GIRAFFE:the tallest animal;PENGUIN:a bird that cannot fly
Jobs in a hospital|DOCTOR:she or he examines patients;NURSE:cares for patients;SURGEON:operates on patients;PHARMACIST:prepares medicine;RECEPTIONIST:greets you at the front desk;PARAMEDIC:rides in the ambulance
Things in a kitchen drawer|SPOON:you eat soup with it;FORK:it has prongs;KNIFE:you cut with it;LADLE:a big spoon for soup;WHISK:you beat eggs with it;SPATULA:you flip burgers with it`.split('\n').map(l=>{ const [cat,r]=l.split('|'); return {cat,words:r.split(';').map(x=>{ const i=x.indexOf(':'); return {w:x.slice(0,i),c:x.slice(i+1)}; })}; }));
 add('blanks',`The world’s laziest superhero only fights crime while ___.|sleeping,napping,sitting,eating,lying down,watching TV
My grandma’s secret recipe calls for a cup of ___.|sugar,love,butter,flour,salt,coffee
The cat refused to come home until we bought it a new ___.|bed,toy,collar,mouse,fish,house
At the science fair, my volcano erupted with ___.|lava,soda,vinegar,foam,glitter,slime
The new phone comes with a free ___.|case,charger,headphones,screen protector,app,game
The haunted house was scariest because of the ___.|ghost,noises,clown,spiders,darkness,basement
The king’s crown was secretly made of ___.|plastic,paper,gold,chocolate,cardboard,tin foil
On vacation, Dad wore socks with ___.|sandals,shorts,flip flops,shoes,crocs,swim trunks
The penguin waddled into the restaurant and ordered ___.|fish,pizza,ice cream,sushi,soup,shrimp
The robot’s first words were “___.”|hello,beep,I am alive,feed me,help,mama
At the talent show, my uncle juggled ___.|balls,eggs,knives,oranges,apples,plates
The dragon’s favorite snack is ___.|knights,popcorn,marshmallows,gold,chicken,pizza
The baby’s first word was “___.”|mama,dada,no,cookie,dog,ball
My boss’s desk is covered in ___.|papers,coffee cups,sticky notes,dust,pictures,snacks
The detective found a clue hidden in the ___.|book,closet,drawer,shoe,garden,attic
Every morning the rooster crows “___.”|cock-a-doodle-doo,wake up,good morning,hello,coffee,breakfast
The astronaut forgot to pack her ___.|helmet,toothbrush,snacks,phone,socks,lunch
Nobody wanted to sit next to the man eating ___.|garlic,onions,fish,tuna,sardines,durian
The magician made the ___ disappear.|rabbit,elephant,car,coin,card,audience
The wedding cake was shaped like a ___.|heart,castle,tower,car,swan,dinosaur`.split('\n').map(l=>{ const [q,a]=l.split('|'); return {q,a:a.split(',')}; }));
 add('tunes',[['Hot Cross Buns','E4 D4 C4:2 E4 D4 C4:2 C4:.5 C4:.5 C4:.5 C4:.5 D4:.5 D4:.5 D4:.5 D4:.5 E4 D4 C4:2'],['This Old Man','G4 E4 G4:2 G4 E4 G4:2 A4 G4 F4 E4 D4 E4 F4:2'],['The Itsy Bitsy Spider','G4 C5 C5 C5 D5 E5:1.5 E5:.5 E5 D5 C5 D5 E5 C5:2'],['Camptown Races','G4 G4 E4 G4 A4 G4 E4:2 E4 D4:2 E4 D4:2'],['Minuet in G','D5 G4:.5 A4:.5 B4:.5 C5:.5 D5 G4 G4 E5 C5:.5 D5:.5 E5:.5 F#5:.5 G5 G4 G4'],['Canon in D (Pachelbel)','F#5:2 E5:2 D5:2 C#5:2 B4:2 A4:2 B4:2 C#5:2'],['Eine kleine Nachtmusik (Mozart)','G4 D4:.5 G4 D4:.5 G4:.5 D4:.5 G4:.5 B4:.5 D5:2'],['Bridal Chorus (Wagner)','C4 F4:1.5 F4:.5 F4:2 C4 G4 E4 F4:2'],['Habanera from Carmen (Bizet)','D5:1.5 C#5:.5 C5 C5 B4:1.5 A#4:.5 A4 G#4 G4'],['The Blue Danube (Strauss)','D4 D4 F#4 A4 A4:2 A5 A5:2 F#5 F#5:2 D4 D4 F#4 A4 A4:2 A5 A5:2 G5 G5:2'],['La Cucaracha','C4:.5 C4:.5 C4:.5 F4:1.5 A4 C4:.5 C4:.5 C4:.5 F4:1.5 A4']]);
})();
