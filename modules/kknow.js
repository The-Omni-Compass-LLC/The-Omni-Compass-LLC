(()=>{ /* 📚 THE KNOWLEDGE LIBRARY (v198): cabinets of learning, each a set of drawers, each drawer a set of cards. Music theory, writing, English,
   psychology, mathematics and games. Every card names the free source it comes from, can be read aloud (with Stop), copied, or saved to Projects. */
 const $=id=>document.getElementById(id); const say=m=>{ try{ toast(m); }catch(_){ } };
 const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const W=a=>'https://en.wikipedia.org/wiki/'+a;
 const MT='https://www.musictheory.net/lessons', OWL='https://owl.purdue.edu/owl/', PSY='https://openstax.org/details/books/psychology-2e', OSM='https://openstax.org/subjects/math', KA='https://www.khanacademy.org/math';
 /* [term, what it is, source name, source link] */
 const CAB=[
 ['music','🎼','Music',[
  ['The basics',[
   ['Pitch and the note names','Western music names its notes A B C D E F G, then repeats them one octave higher. Sharps (♯) raise a note a half step and flats (♭) lower it; on a piano the twelve keys from one C to the next are the twelve half steps of an octave.','musictheory.net lessons',MT],
   ['Octave','The distance from one note to the next note of the same name. The higher note vibrates exactly twice as fast, which is why the two sound like the same note at different heights.','Wikipedia: Octave',W('Octave')],
   ['Interval','The distance between two notes, counted in letter names and half steps: a major third is four half steps (C to E), a perfect fifth is seven (C to G).','Wikipedia: Interval',W('Interval_(music)')],
   ['Tempo and BPM','How fast the music moves, in beats per minute. 60 BPM is one beat a second; most pop and hip-hop sits between about 70 and 140.','Wikipedia: Tempo',W('Tempo')],
   ['Dynamics','How loud or soft the music is played: from pianissimo (pp, very soft) through mezzo-forte (mf) to fortissimo (ff, very loud).','Wikipedia: Dynamics',W('Dynamics_(music)')]]],
  ['Scales and modes',[
   ['Major scale','Seven notes in the pattern whole, whole, half, whole, whole, whole, half. C major uses only the white keys: C D E F G A B.','musictheory.net lessons',MT],
   ['Natural minor scale','The pattern whole, half, whole, whole, half, whole, whole. A minor shares its notes with C major but starts on A, so it sounds darker.','Wikipedia: Minor scale',W('Minor_scale')],
   ['The modes','Seven scales made by starting the major scale on each of its notes: Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian and Locrian. Dorian sounds soulful, Mixolydian bluesy, Phrygian dark and Spanish.','Wikipedia: Mode',W('Mode_(music)')],
   ['Pentatonic scale','A five-note scale, found in folk music the world over. The minor pentatonic is the heart of blues, rock and many hip-hop melodies.','Wikipedia: Pentatonic scale',W('Pentatonic_scale')],
   ['Circle of fifths','The twelve keys arranged so each is a fifth above the last. Neighbours on the circle share all but one note, so moving between them sounds smooth.','Wikipedia: Circle of fifths',W('Circle_of_fifths')]]],
  ['Chords and harmony',[
   ['Triad','A three-note chord built in thirds: root, third and fifth. A major triad (C E G) sounds bright; a minor triad (C E♭ G) sounds darker.','musictheory.net lessons',MT],
   ['Seventh chords','A triad with a fourth note a seventh above the root. Major sevenths sound lush, minor sevenths smooth, and dominant sevenths pull toward home.','Wikipedia: Seventh chord',W('Seventh_chord')],
   ['Roman numerals','Chords are named by the scale step they stand on: in C major, I is C, IV is F, V is G and vi is A minor. The same numbers work in every key.','Wikipedia: Roman numeral analysis',W('Roman_numeral_analysis')],
   ['Chord progression','A series of chords. I–V–vi–IV carries thousands of pop songs; ii–V–I is the backbone of jazz; i–♭VII–♭VI–V is the Andalusian cadence.','Wikipedia: Chord progression',W('Chord_progression')],
   ['Cadence','The chords that end a phrase. An authentic cadence (V to I) sounds finished; a half cadence stops on V and leaves the listener waiting.','Wikipedia: Cadence',W('Cadence')]]],
  ['Rhythm and meter',[
   ['Time signature','The two numbers at the start of the music: the top says how many beats are in a bar, the bottom which note gets the beat. 4/4 is four quarter-note beats a bar.','Wikipedia: Time signature',W('Time_signature')],
   ['Downbeat and backbeat','The downbeat is the first beat of the bar, where the kick usually lands. The backbeat is beats two and four, where the snare or clap lands in most pop, rock and hip-hop.','Wikipedia: Beat',W('Beat_(music)')],
   ['Syncopation','Accenting the off-beats, the places between the main beats. It makes a groove feel like it pushes and pulls.','Wikipedia: Syncopation',W('Syncopation')],
   ['Swing','Playing pairs of even notes long-short instead of even, which gives jazz, shuffle and many hip-hop beats their lilt.','Wikipedia: Swing',W('Swing_(jazz_performance_style)')],
   ['Euclidean rhythm','A rhythm made by spreading a number of hits as evenly as possible over a number of steps. Three hits over eight steps gives the tresillo heard across Latin and pop music.','Wikipedia: Euclidean rhythm',W('Euclidean_rhythm')]]],
  ['Song form',[
   ['Verse and chorus','The verse tells the story and changes its words each time; the chorus is the repeated hook that carries the title.','Wikipedia: Song structure',W('Song_structure')],
   ['Pre-chorus and bridge','A pre-chorus builds tension into the chorus. A bridge brings something new, often new chords, before the last chorus.','Wikipedia: Song structure',W('Song_structure')],
   ['Hook','The catchiest part of a song, the part people remember: a line, a melody or a sound.','Wikipedia: Hook',W('Hook_(music)')],
   ['Twelve-bar blues','A twelve-bar form over the I, IV and V chords that underlies blues, early rock and roll and much of jazz.','Wikipedia: Twelve-bar blues',W('Twelve-bar_blues')]]],
  ['Mixing and production',[
   ['Equalization (EQ)','Turning frequency ranges up or down: cutting low rumble, giving a vocal presence, taming harsh highs.','Wikipedia: Equalization',W('Equalization_(audio)')],
   ['Compression','Narrowing the gap between the loud and soft parts of a sound so it sits steady in the mix. Sidechain compression lets a kick push the other parts down for a pumping feel.','Wikipedia: Dynamic range compression',W('Dynamic_range_compression')],
   ['Reverb and delay','Reverb places a sound in a space, from a small room to a cathedral. Delay repeats it as echoes, often in time with the beat.','Wikipedia: Reverberation',W('Reverberation')],
   ['Panning and stereo','Placing each sound from left to right. Wide parts and a centred kick, bass and vocal give a clear mix.','Wikipedia: Panning',W('Panning_(audio)')],
   ['Sampling','Reusing a piece of an existing recording as an instrument. Sampling a record someone else owns needs permission; KAN-IN’s recorded library is CC0, free to use.','Wikipedia: Sampling',W('Sampling_(music)')]]]]],
 ['writing','✍️','Writing',[
  ['Story structure',[
   ['Three-act structure','Setup, confrontation and resolution. The first act sets up the world and the problem, the second raises the stakes, the third resolves them.','Wikipedia: Three-act structure',W('Three-act_structure')],
   ['Freytag’s pyramid','Exposition, rising action, climax, falling action and resolution: Gustav Freytag’s 1863 map of a drama’s shape.','Wikipedia: Dramatic structure',W('Dramatic_structure')],
   ['The hero’s journey','Joseph Campbell’s pattern of the call to adventure, the trials, the ordeal and the return home changed. Many myths and films follow it loosely.','Wikipedia: Hero’s journey',W('Hero%27s_journey')],
   ['Inciting incident','The event that knocks the hero’s ordinary life off balance and starts the story moving.','Wikipedia: Inciting incident',W('Inciting_incident')],
   ['In medias res','Starting the story in the middle of the action, then filling in what came before.','Wikipedia: In medias res',W('In_medias_res')]]],
  ['Character',[
   ['Want and need','What a character wants is the goal they chase; what they need is the lesson that would heal them. The best stories make the two pull against each other.','Purdue OWL: Creative writing',OWL],
   ['Character arc','How a character changes from the first page to the last: growing, falling or staying firm while the world changes around them.','Wikipedia: Character arc',W('Character_arc')],
   ['Protagonist and antagonist','The protagonist drives the story; the antagonist, a person, a force or a flaw, stands in their way.','Wikipedia: Protagonist',W('Protagonist')],
   ['Show, don’t tell','Letting readers see a feeling in action and detail (“her hands shook”) rather than naming it (“she was nervous”).','Wikipedia: Show, don’t tell',W('Show,_don%27t_tell')]]],
  ['Point of view and voice',[
   ['First person','The narrator is a character and says “I”. Close and personal, but the reader knows only what the narrator knows.','Wikipedia: Narration',W('Narration')],
   ['Third person limited','“He” or “she”, staying close to one character’s thoughts at a time.','Wikipedia: Narration',W('Narration')],
   ['Third person omniscient','A narrator who can see into every character and every place.','Wikipedia: Narration',W('Narration')],
   ['Unreliable narrator','A narrator whose account cannot be fully trusted, by mistake or on purpose.','Wikipedia: Unreliable narrator',W('Unreliable_narrator')]]],
  ['Literary devices',[
   ['Metaphor and simile','A metaphor says one thing is another (“the city is a jungle”); a simile says it is like another (“the city is like a jungle”).','Wikipedia: Metaphor',W('Metaphor')],
   ['Foreshadowing','Planting hints early of what will happen later.','Wikipedia: Foreshadowing',W('Foreshadowing')],
   ['Chekhov’s gun','Every important detail shown should matter later: if a gun hangs on the wall in act one, it should go off by act three.','Wikipedia: Chekhov’s gun',W('Chekhov%27s_gun')],
   ['Irony','A gap between what is said or expected and what is meant or happens. Dramatic irony is when the audience knows something a character does not.','Wikipedia: Irony',W('Irony')],
   ['Alliteration','Repeating the first sound of nearby words: “Peter Piper picked a peck”.','Wikipedia: Alliteration',W('Alliteration')]]],
  ['Poetry and lyrics',[
   ['Rhyme scheme','The pattern of rhymes at the ends of lines, written with letters: ABAB, AABB, ABCB.','Wikipedia: Rhyme scheme',W('Rhyme_scheme')],
   ['Meter and the iamb','The beat of a line. An iamb is a soft syllable then a strong one (da-DUM); five of them make iambic pentameter, Shakespeare’s line.','Wikipedia: Iambic pentameter',W('Iambic_pentameter')],
   ['Internal and multisyllabic rhyme','Rhymes inside the line, and rhymes of two or more syllables. Both are central to rap.','Wikipedia: Internal rhyme',W('Internal_rhyme')],
   ['Haiku','A Japanese form of three lines, traditionally of 5, 7 and 5 sound units, usually tied to a season.','Wikipedia: Haiku',W('Haiku')]]],
  ['Screenwriting',[
   ['Logline','The whole story in one or two sentences: the hero, the goal, the obstacle and the stakes.','Wikipedia: Log line',W('Log_line')],
   ['Slug line','The heading of every scene: INT. or EXT., the place and the time of day.','Wikipedia: Screenplay',W('Screenplay')],
   ['Screenplay page','Set in Courier 12 pt, a screenplay page runs about one minute of screen time.','Wikipedia: Screenplay',W('Screenplay')]]]]],
 ['english','📘','English',[
  ['Parts of speech',[
   ['Noun and pronoun','A noun names a person, place, thing or idea; a pronoun (he, she, they, it) stands in for one.','Purdue OWL',OWL],
   ['Verb','A word for an action or a state: run, think, is. Every complete sentence has one.','Wikipedia: Verb',W('Verb')],
   ['Adjective and adverb','Adjectives describe nouns (a red car); adverbs describe verbs, adjectives or other adverbs (drove quickly, very red).','Wikipedia: Part of speech',W('Part_of_speech')],
   ['Preposition and conjunction','Prepositions show relation (in, on, under, after); conjunctions join words and clauses (and, but, or, because).','Wikipedia: Part of speech',W('Part_of_speech')]]],
  ['Punctuation',[
   ['Comma','Separates items in a list, sets off introductory words, and joins two complete sentences with and, but, or, so.','Purdue OWL: Commas',OWL],
   ['Serial (Oxford) comma','The comma before the last item of a list: red, white, and blue. Style guides differ; whichever you choose, keep it consistent.','Wikipedia: Serial comma',W('Serial_comma')],
   ['Semicolon','Joins two closely related complete sentences without a conjunction: It rained; we stayed in.','Wikipedia: Semicolon',W('Semicolon')],
   ['Apostrophe','Shows possession (the cat’s toy) or a missing letter (don’t). It is never used to make a plain plural: one cat, two cats.','Wikipedia: Apostrophe',W('Apostrophe')],
   ['Colon and dash','A colon introduces what follows (a list, an explanation); a dash marks a sudden break or adds emphasis.','Purdue OWL',OWL]]],
  ['Sentences',[
   ['Subject and predicate','The subject is who or what the sentence is about; the predicate says what it does or is.','Wikipedia: Predicate',W('Predicate_(grammar)')],
   ['Clause','A group of words with a subject and a verb. An independent clause can stand alone; a dependent clause (because it rained) cannot.','Wikipedia: Clause',W('Clause')],
   ['Run-on and fragment','A run-on jams two sentences together without the right punctuation; a fragment is missing a subject or a verb.','Purdue OWL',OWL],
   ['Active and passive voice','Active: the dog chased the ball. Passive: the ball was chased by the dog. Active is usually clearer and shorter.','Wikipedia: Active voice',W('Active_voice')],
   ['Dangling modifier','A describing phrase attached to the wrong word: “Walking home, the rain started.” (The rain was not walking.)','Wikipedia: Dangling modifier',W('Dangling_modifier')]]],
  ['Words often confused',[
   ['Their, there, they’re','Their = belonging to them. There = that place. They’re = they are.','Wiktionary','https://en.wiktionary.org/wiki/their'],
   ['Your and you’re','Your = belonging to you. You’re = you are.','Wiktionary','https://en.wiktionary.org/wiki/your'],
   ['Its and it’s','Its = belonging to it. It’s = it is or it has.','Wiktionary','https://en.wiktionary.org/wiki/its'],
   ['Affect and effect','Affect is usually the verb (the song affects me); effect is usually the noun (the song has an effect on me).','Wiktionary','https://en.wiktionary.org/wiki/affect'],
   ['Then and than','Then is about time (first this, then that); than compares (taller than me).','Wiktionary','https://en.wiktionary.org/wiki/than']]]]],
 ['psych','🧠','Psychology',[
  ['Memory and learning',[
   ['Working memory','The mind’s small notepad that holds what you are thinking about right now. It holds only a few items at once, so big tasks go better in small steps.','Wikipedia: Working memory',W('Working_memory')],
   ['Forgetting curve','Hermann Ebbinghaus found that new learning fades fast in the first hours and days unless it is reviewed.','Wikipedia: Forgetting curve',W('Forgetting_curve')],
   ['Spacing effect','Studying in several short sessions spread over time beats one long session of the same length.','Wikipedia: Spacing effect',W('Spacing_effect')],
   ['Testing effect','Trying to recall something, as in a quiz, strengthens memory more than reading it again.','Wikipedia: Testing effect',W('Testing_effect')]]],
  ['Motivation and emotion',[
   ['Intrinsic and extrinsic motivation','Intrinsic motivation is doing something because it is satisfying in itself; extrinsic is doing it for a reward or to avoid a penalty.','OpenStax Psychology 2e',PSY],
   ['Maslow’s hierarchy of needs','Abraham Maslow’s model of needs from the physical, through safety, belonging and esteem, to self-actualization. It is a popular model, and research supports it only in part.','Wikipedia: Maslow’s hierarchy',W('Maslow%27s_hierarchy_of_needs')],
   ['Flow','Mihaly Csikszentmihalyi’s name for being fully absorbed in a task whose challenge matches your skill.','Wikipedia: Flow',W('Flow_(psychology)')],
   ['Growth mindset','Carol Dweck’s idea that believing abilities can grow with effort helps people keep learning. Later studies find its effects real but often small.','Wikipedia: Mindset',W('Mindset')]]],
  ['Thinking and bias',[
   ['Confirmation bias','The habit of noticing and trusting what agrees with what we already believe.','Wikipedia: Confirmation bias',W('Confirmation_bias')],
   ['Anchoring','The first number we see pulls later estimates toward it, even when it is unrelated.','Wikipedia: Anchoring effect',W('Anchoring_effect')],
   ['Availability heuristic','Judging how likely something is by how easily examples come to mind, which makes vivid events seem more common than they are.','Wikipedia: Availability heuristic',W('Availability_heuristic')],
   ['Dunning–Kruger effect','People with little skill in an area tend to overrate their ability in it.','Wikipedia: Dunning–Kruger effect',W('Dunning%E2%80%93Kruger_effect')]]],
  ['Development',[
   ['Piaget’s stages','Jean Piaget’s four stages of thinking in childhood: sensorimotor, preoperational, concrete operational and formal operational.','Wikipedia: Piaget’s theory',W('Piaget%27s_theory_of_cognitive_development')],
   ['Erikson’s stages','Erik Erikson’s eight stages across the whole life, each a challenge such as trust against mistrust or identity against role confusion.','Wikipedia: Erikson’s stages',W('Erikson%27s_stages_of_psychosocial_development')],
   ['Attachment','The bond between a child and the people who care for them, which shapes how safe the child feels to explore.','Wikipedia: Attachment theory',W('Attachment_theory')]]],
  ['People together',[
   ['Social proof','People look to what others are doing to decide what is right, especially when unsure.','Wikipedia: Social proof',W('Social_proof')],
   ['Bystander effect','People are less likely to help in an emergency when others are present, each expecting someone else to act.','Wikipedia: Bystander effect',W('Bystander_effect')],
   ['Cognitive dissonance','The discomfort of holding two beliefs that clash, or acting against a belief, and the urge to ease it.','Wikipedia: Cognitive dissonance',W('Cognitive_dissonance')],
   ['Mere-exposure effect','People tend to like things more the more often they meet them, songs included.','Wikipedia: Mere-exposure effect',W('Mere-exposure_effect')]]],
  ['Creativity',[
   ['Divergent thinking','Producing many different ideas from one starting point, as in brainstorming. Convergent thinking then picks the best one.','Wikipedia: Divergent thinking',W('Divergent_thinking')],
   ['Incubation','Stepping away from a problem for a while often helps a solution appear later.','Wikipedia: Incubation',W('Incubation_(psychology)')],
   ['Constraints','Limits, a word count, a form, a set of sounds, often make people more creative, not less.','OpenStax Psychology 2e',PSY]]]]],
 ['math','➗','Mathematics',[
  ['Numbers',[
   ['Order of operations','Brackets first, then exponents, then multiplication and division from left to right, then addition and subtraction from left to right. 2 + 3 × 4 = 14.','Wikipedia: Order of operations',W('Order_of_operations')],
   ['Prime numbers','Whole numbers above 1 divisible only by 1 and themselves: 2, 3, 5, 7, 11, 13… Every whole number above 1 is a product of primes in exactly one way.','Wikipedia: Prime number',W('Prime_number')],
   ['Fractions, decimals and percentages','Three ways to write a part of a whole: ½ = 0.5 = 50%. A percentage is a fraction out of 100.','Khan Academy',KA],
   ['Ratio','A comparison of two amounts: 3 : 2. Musical intervals are ratios of frequencies: the octave is 2 : 1, the perfect fifth about 3 : 2.','Wikipedia: Ratio',W('Ratio')]]],
  ['Algebra',[
   ['Variables and equations','A letter stands for an unknown number; an equation says two expressions are equal. Whatever you do to one side, do to the other.','OpenStax math',OSM],
   ['Linear equation','A straight line: y = mx + b, where m is the slope and b where the line crosses the y-axis.','Wikipedia: Linear equation',W('Linear_equation')],
   ['Quadratic formula','For ax² + bx + c = 0, x = (−b ± √(b² − 4ac)) ÷ 2a.','Wikipedia: Quadratic formula',W('Quadratic_formula')],
   ['Exponents','Repeated multiplication: 2⁵ = 2 × 2 × 2 × 2 × 2 = 32. Doubling a loop five times from one bar gives 2⁵ = 32 bars.','Khan Academy',KA]]],
  ['Geometry',[
   ['Pythagorean theorem','In a right triangle, a² + b² = c², where c is the side opposite the right angle.','Wikipedia: Pythagorean theorem',W('Pythagorean_theorem')],
   ['Circle','Circumference = 2πr; area = πr². π is about 3.14159.','Wikipedia: Circle',W('Circle')],
   ['Angles','A full turn is 360°, a straight line 180°, a right angle 90°. The angles of a triangle add up to 180°.','OpenStax math',OSM]]],
  ['Chance and data',[
   ['Probability','The chance of an event, from 0 (impossible) to 1 (certain): favourable outcomes ÷ all equally likely outcomes. A fair die shows a six with probability 1/6.','Wikipedia: Probability',W('Probability')],
   ['Expected value','The long-run average of a chance event: each outcome times its probability, added up. The expected roll of one die is 3.5.','Wikipedia: Expected value',W('Expected_value')],
   ['Law of large numbers','The more times you repeat a chance event, the closer the average comes to the expected value.','Wikipedia: Law of large numbers',W('Law_of_large_numbers')],
   ['Mean, median and mode','The mean is the sum divided by the count; the median is the middle value in order; the mode is the most common value.','Khan Academy',KA],
   ['Standard deviation','How spread out a set of numbers is around its mean.','Wikipedia: Standard deviation',W('Standard_deviation')],
   ['Permutations and combinations','Ways to arrange or choose things. Arranging n things gives n! orders (3! = 6); choosing k of n, order not mattering, is n! ÷ (k!(n − k)!).','Wikipedia: Combination',W('Combination')]]],
  ['Math in music and art',[
   ['Equal temperament','Modern tuning splits the octave into 12 equal half steps; each is the twelfth root of 2 (about 1.0595) times the one below.','Wikipedia: 12 equal temperament',W('12_equal_temperament')],
   ['Fibonacci sequence','1, 1, 2, 3, 5, 8, 13…, each number the sum of the two before it. Its ratios approach the golden ratio, about 1.618.','Wikipedia: Fibonacci sequence',W('Fibonacci_sequence')],
   ['Symmetry','A shape or pattern that stays the same when mirrored, turned or shifted, in art, crystals and rhythm alike.','Wikipedia: Symmetry',W('Symmetry')]]]]],
 ['games','🎲','Games',[
  ['Game design',[
   ['Game mechanics','The rules and actions a player can take, and how the game answers them.','Wikipedia: Game mechanics',W('Game_mechanics')],
   ['Core loop','The action the player repeats again and again, such as aim, fire, score, which carries most of the fun.','Wikipedia: Game mechanics',W('Game_mechanics')],
   ['Balance','Making sure no single strategy, character or move always wins, so choices stay interesting.','Wikipedia: Game balance',W('Game_balance')],
   ['Difficulty curve','How the challenge rises as the player improves: too flat is boring, too steep is frustrating.','Wikipedia: Game difficulty',W('Game_difficulty')]]],
  ['Strategy',[
   ['Zero-sum game','A game where one player’s gain is exactly another’s loss, as in chess or poker.','Wikipedia: Zero-sum game',W('Zero-sum_game')],
   ['Nash equilibrium','A set of choices where no player can do better by changing only their own move.','Wikipedia: Nash equilibrium',W('Nash_equilibrium')],
   ['Minimax','Choosing the move whose worst possible result is the best; the basis of many board-game computer players.','Wikipedia: Minimax',W('Minimax')],
   ['Tempo and initiative','In board games, being the player who makes threats while the other must answer them.','Wikipedia: Initiative',W('Initiative_(chess)')]]],
  ['Chance in games',[
   ['Two dice','Rolling two dice, 7 is the most likely total (6 ways in 36, 1/6) and 2 and 12 the least (1 way each, 1/36).','Wikipedia: Dice',W('Dice')],
   ['Gambler’s fallacy','The mistaken belief that past results change the odds of independent events: after five heads, the next fair coin toss is still 50-50.','Wikipedia: Gambler’s fallacy',W('Gambler%27s_fallacy')],
   ['Monty Hall problem','Three doors, one prize. After the host opens an empty door, switching wins 2/3 of the time and staying only 1/3.','Wikipedia: Monty Hall problem',W('Monty_Hall_problem')],
   ['House edge','In casino games the rules give the house a small built-in advantage, so over many plays the house comes out ahead. KAN-IN’s casino uses play chips only.','Wikipedia: Casino game',W('Casino_game')]]],
  ['Classic games',[
   ['Chess','Two players, sixteen pieces each, on an 8 × 8 board. The goal is checkmate: the king is attacked and cannot escape.','Wikipedia: Rules of chess',W('Rules_of_chess')],
   ['Checkers (draughts)','Pieces move diagonally forward and jump to capture; a piece that reaches the far row becomes a king and moves both ways.','Wikipedia: English draughts',W('English_draughts')],
   ['Go','Two players place black and white stones to surround territory on a 19 × 19 grid; stones fully surrounded are captured.','Wikipedia: Go',W('Go_(game)')],
   ['Mancala','A family of “count and capture” games where seeds are sown around pits on a board, played across Africa and Asia for centuries.','Wikipedia: Mancala',W('Mancala')],
   ['Tic-tac-toe','Three in a row on a 3 × 3 grid. With perfect play by both players it always ends in a draw.','Wikipedia: Tic-tac-toe',W('Tic-tac-toe')]]],
  ['Puzzles',[
   ['Sudoku','Fill a 9 × 9 grid so every row, column and 3 × 3 box holds 1 to 9 once each.','Wikipedia: Sudoku',W('Sudoku')],
   ['Tower of Hanoi','Move a stack of discs to another peg, one disc at a time, never a larger one on a smaller. n discs take 2ⁿ − 1 moves at best.','Wikipedia: Tower of Hanoi',W('Tower_of_Hanoi')],
   ['Nonogram','A picture puzzle: the numbers beside each row and column say how many filled cells run together there.','Wikipedia: Nonogram',W('Nonogram')]]]]]];
 const COUNT=CAB.reduce((a,c)=>a+c[3].reduce((b,d)=>b+d[1].length,0),0);
 let cab=null, q='';
 const css=document.createElement('style'); css.textContent=`
#kKnow{position:fixed;inset:0;z-index:9700;background:rgba(5,6,22,.97);overflow:auto;color:#fff;padding:14px 16px calc(230px + env(safe-area-inset-bottom,0px));padding-right:calc(var(--kRailW,58px) + 16px)}
#kKnow[hidden]{display:none!important}
#kKnow .knIn{max-width:920px;margin:0 auto}
#kKnow .knN{font-size:12.5px;opacity:.85;line-height:1.5}
#kKnow .knCabs{display:grid;grid-template-columns:repeat(auto-fill,minmax(128px,1fr));gap:8px;margin:10px 0}
#kKnow .knCabs button{min-height:58px!important;border-radius:14px!important;font-size:14px!important;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
#kKnow .knCabs button[aria-pressed="true"]{background:#137a3f!important}
#kKnow .knCabs button span{font-size:22px}
#kKnow details{border:1px solid rgba(255,255,255,.18);border-radius:12px;margin:8px 0;background:rgba(255,255,255,.03)}
#kKnow summary{cursor:pointer;padding:10px 12px;font-weight:800;color:#ffe94a;min-height:24px}
#kKnow .knCard{border-top:1px solid rgba(255,255,255,.1);padding:10px 12px}
#kKnow .knCard b{display:block;font-size:15px;margin-bottom:3px}
#kKnow .knCard p{margin:0 0 6px;line-height:1.55;font-size:14px}
#kKnow .knRow{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
#kKnow .knRow button{min-height:36px!important;padding:4px 10px!important;font-size:12.5px!important}
#kKnow .knRow a{color:#7fe0ff;font-size:12.5px}
#kKnow input[type=search]{width:100%;max-width:520px;min-height:40px;font-size:15px;padding:6px 10px;border-radius:10px}`; document.head.appendChild(css);
 function box(){ let d=$('kKnow'); if(d) return d; d=document.createElement('div'); d.id='kKnow'; d.setAttribute('role','dialog'); d.setAttribute('aria-label','Knowledge library'); d.hidden=true; document.body.appendChild(d);
  d.addEventListener('click',onClick); d.addEventListener('input',e=>{ if(e.target.id==='knQ'){ q=e.target.value; paintList(); } }); return d; }
 const match=(c)=>{ if(!q.trim()) return true; const t=(c[0]+' '+c[1]).toLowerCase(); return q.toLowerCase().split(/\s+/).filter(Boolean).every(w=>t.includes(w)); };
 function cardHTML(c,id){ return '<div class="knCard"><b>'+esc(c[0])+'</b><p>'+esc(c[1])+'</p><div class="knRow"><button type="button" data-kn="read" data-id="'+id+'" data-noul>🔊 Read</button><button type="button" data-kn="stop" data-noul>⏹ Stop</button><button type="button" data-kn="copy" data-id="'+id+'" data-noul>📋 Copy</button><button type="button" data-kn="save" data-id="'+id+'" data-noul>📁 Save to Projects</button><a href="'+esc(c[3])+'" target="_blank" rel="noopener noreferrer">Source: '+esc(c[2])+' ↗</a></div></div>'; }
 const find=id=>{ const [a,b,c]=id.split('.').map(Number); return CAB[a][3][b][1][c]; };
 function paintList(){ const L=$('knList'); if(!L) return; let html='', n=0;
  CAB.forEach((C,a)=>{ if(cab!=null&&cab!==a&&!q.trim()) return; C[3].forEach((D,b)=>{ const cards=D[1].map((c,i)=>[c,a+'.'+b+'.'+i]).filter(([c])=>match(c)); if(!cards.length) return; n+=cards.length; html+='<details'+(q.trim()?' open':'')+'><summary>'+C[1]+' '+esc(C[2])+' · '+esc(D[0])+' <span class="knN">('+cards.length+')</span></summary>'+cards.map(([c,id])=>cardHTML(c,id)).join('')+'</details>'; }); });
  L.innerHTML=html||'<p class="knN">Nothing found. Try another word.</p>'; const s=$('knCount'); if(s) s.textContent=q.trim()?n+' card'+(n===1?'':'s')+' found':''; }
 function paint(){ const d=box(); d.innerHTML='<div class="kBar" data-sc="kKnow"><button type="button" data-ka="close" data-kn="close" aria-label="Close">✕</button></div><div class="knIn"><div class="knN">The Omni-Compass LLC · DD Universe Multi-Media Studios’ KAN-IN™ · Knowledge library</div><h2>📚 The knowledge library</h2><p class="knN">'+COUNT+' cards in '+CAB.length+' cabinets: music theory, writing, English, psychology, mathematics and games. Every card names the free source it comes from; tap the source to read further. Read any card aloud, copy it, or save it to your Projects.</p><input type="search" id="knQ" placeholder="Search every card, for example: chord, comma, memory, probability" aria-label="Search the knowledge library" value="'+esc(q)+'"> <span class="knN" id="knCount"></span><div class="knCabs">'+CAB.map((C,a)=>'<button type="button" data-kn="cab" data-a="'+a+'" aria-pressed="'+(cab===a)+'" data-noul><span>'+C[1]+'</span>'+esc(C[2])+'</button>').join('')+'<button type="button" data-kn="cab" data-a="-1" aria-pressed="'+(cab==null)+'" data-noul><span>🗄</span>Every cabinet</button></div><div id="knList"></div></div>'; paintList(); }
 async function onClick(e){ const b=e.target.closest('[data-kn]'); if(!b) return; const k=b.dataset.kn;
  if(k==='close') return close(); if(k==='cab'){ const a=+b.dataset.a; cab=a<0?null:a; q=''; return paint(); }
  if(k==='stop'){ try{ speechSynthesis.cancel(); }catch(_){ } return; }
  const c=find(b.dataset.id); if(!c) return; const text=c[0]+'. '+c[1];
  if(k==='read'){ try{ speechSynthesis.cancel(); const u=new SpeechSynthesisUtterance(text); try{ const v=window.KVOICE&&KVOICE('en'); if(v) u.voice=v; }catch(_){ } speechSynthesis.speak(u); }catch(_){ say('Read-aloud is not available on this device.'); } return; }
  if(k==='copy'){ try{ await navigator.clipboard.writeText(text+'\nSource: '+c[2]+' '+c[3]); say('📋 Copied.'); }catch(_){ say('Copy was blocked here: select the text and copy it by hand.'); } return; }
  if(k==='save'){ try{ await KLIB.save({kind:'file',name:'Note · '+c[0],blob:new Blob([text+'\n\nSource: '+c[2]+'\n'+c[3]+'\n'],{type:'text/plain'}),meta:{from:'knowledge'}}); say('📁 Saved to your Projects: Note · '+c[0]+'.'); }catch(_){ say('This card could not be saved on this device.'); } return; } }
 function open(c){ const d=box(); try{ ['libDock','fileDock','kManual','kMe','kCan','kDay','kHumor','kJump','kKara','kOwner','kVG','kSocial','kAI','kEasel','kProj','kLock'].forEach(i=>{ const x=$(i); if(x) x.hidden=true; }); }catch(_){ } try{ LAUNCHPAD.fold(); }catch(_){ } try{ (window.__kGoHome0||function(){})(); }catch(_){ }
  if(typeof c==='string'){ const a=CAB.findIndex(C=>C[0]===c); cab=a<0?null:a; } d.hidden=false; d.scrollTop=0; paint(); }
 function close(){ const d=$('kKnow'); if(d) d.hidden=true; try{ speechSynthesis.cancel(); }catch(_){ } }
 document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&$('kKnow')&&!$('kKnow').hidden) close(); });
 try{ const gh=window.GOHOME; if(gh&&!gh.__kkn){ const w=function(){ close(); return gh.apply(this,arguments); }; w.__kkn=1; Object.keys(gh).forEach(k=>{ w[k]=gh[k]; }); window.GOHOME=w; } }catch(_){ }
 document.addEventListener('click',e=>{ if(!e.target.closest) return; if(e.target.closest('#kdHome,#lpMenu')) return close(); const r=e.target.closest('#rDock button,#tourTab button'); if(r&&r.id!=='ttKnow'&&$('kKnow')&&!$('kKnow').hidden) close(); },true);
 setInterval(()=>{ const t=$('tourTab'); if(!t||$('ttKnow')) return; const b=document.createElement('button'); b.type='button'; b.id='ttKnow'; b.className='ttMusic'; b.textContent='📚 Knowledge library · music, writing, English, psychology, math, games'; b.style.order='102'; b.dataset.kg='0'; b.dataset.kmDone='1'; b.setAttribute('data-noul',''); b.style.gridColumn='1/-1'; b.addEventListener('click',e=>{ e.stopPropagation(); try{ LAUNCHPAD.fold(); }catch(_){ } setTimeout(()=>open(),120); }); t.appendChild(b); },900);
 window.KKNOW={open,close,get count(){ return COUNT; },CAB};
})();
