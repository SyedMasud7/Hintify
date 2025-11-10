"""Question data for seeding - 180 questions total"""

TECHNOLOGY_EASY = [
    ("What does CPU stand for?", {"A": ("Central Processing Unit", True), "B": ("Computer Personal Unit", False), "C": ("Central Program Unit", False), "D": ("Computer Processing Unit", False)}, "Think about the 'brain' of the computer - the component that executes instructions and performs calculations. The word 'Central' indicates its primary role, 'Processing' refers to computation, and 'Unit' means it's a single component.", "CPU stands for Central Processing Unit. It's the primary component of a computer that performs most of the processing operations. Think of it as the brain of the computer - it executes instructions from programs, performs calculations, and coordinates all other hardware components. Modern CPUs can execute billions of instructions per second!"),
    ("Which company developed Windows?", {"A": ("Apple", False), "B": ("Microsoft", True), "C": ("Google", False), "D": ("IBM", False)}, "Think about the company founded by Bill Gates and Paul Allen in 1975. This company's name combines 'microcomputer' and 'software'. They created the most widely used desktop operating system in the world.", "Microsoft developed Windows. Founded by Bill Gates and Paul Allen in 1975, Microsoft released Windows 1.0 in 1985 as a graphical operating system shell for MS-DOS. Today, Windows powers over 75% of desktop computers worldwide and has evolved through many versions including Windows 95, XP, 7, 10, and 11."),
    ("What does HTML stand for?", {"A": ("Hyper Text Markup Language", True), "B": ("High Tech Modern Language", False), "C": ("Home Tool Markup Language", False), "D": ("Hyperlinks Text Language", False)}, "This is the standard language for creating web pages. 'Hyper' refers to hyperlinks that connect pages, 'Text' is the content, 'Markup' means tags that structure content, and 'Language' indicates it's a coding system.", "HTML stands for Hyper Text Markup Language. It's the standard markup language for creating web pages and web applications. 'Hyper Text' refers to text with hyperlinks, 'Markup' means using tags to structure content (like <p> for paragraphs), and 'Language' indicates it's a system of communication. HTML was created by Tim Berners-Lee in 1991 and forms the backbone of every website you visit!"),
    ("Main function of RAM?", {"A": ("Permanent storage", False), "B": ("Temporary storage", True), "C": ("Processing", False), "D": ("Graphics", False)}, "RAM stands for Random Access Memory. Think about what happens when you turn off your computer - does the data in RAM stay or disappear? This tells you whether it's permanent or temporary. RAM is like your computer's short-term memory or workspace.", "RAM provides temporary storage for data and programs currently in use. Unlike permanent storage (hard drives/SSDs), RAM is volatile memory - it loses all data when power is turned off. Think of RAM as your computer's workspace: the more RAM you have, the more programs you can run simultaneously without slowing down. When you open an application, it loads from storage into RAM for fast access by the CPU."),
    ("Which is a programming language?", {"A": ("HTTP", False), "B": ("Python", True), "C": ("HTML", False), "D": ("USB", False)}, "Look for the option that's used to write instructions for computers to execute. Named after the British comedy group Monty Python (not the snake!), this language is known for its simple, readable syntax and is widely used in web development, data science, and AI.", "Python is a programming language. Created by Guido van Rossum in 1991, Python is a high-level, interpreted language known for its simple, readable syntax. It's named after Monty Python's Flying Circus, not the snake! Python is versatile and used in web development (Django, Flask), data science (pandas, NumPy), machine learning (TensorFlow, PyTorch), automation, and more. Its philosophy emphasizes code readability with significant whitespace."),
    ("What does URL stand for?", {"A": ("Uniform Resource Locator", True), "B": ("Universal Resource Link", False), "C": ("Unified Resource Location", False), "D": ("Universal Reference Link", False)}, "Web address.", "URL is Uniform Resource Locator."),
    ("Copy shortcut?", {"A": ("Ctrl+X", False), "B": ("Ctrl+V", False), "C": ("Ctrl+C", True), "D": ("Ctrl+Z", False)}, "C for Copy.", "Ctrl+C copies text."),
    ("Binary system based on?", {"A": ("0 and 1", True), "B": ("1 and 2", False), "C": ("0 to 9", False), "D": ("A to Z", False)}, "Two digits only.", "Binary uses 0 and 1."),
    ("What does Wi-Fi stand for?", {"A": ("Wireless Fidelity", True), "B": ("Wired Fiber", False), "C": ("Wide Field", False), "D": ("Wireless Field", False)}, "Like Hi-Fi.", "Wi-Fi is Wireless Fidelity."),
    ("Who created iPhone?", {"A": ("Samsung", False), "B": ("Apple", True), "C": ("Google", False), "D": ("Microsoft", False)}, "Fruit logo.", "Apple created iPhone."),
    ("Purpose of firewall?", {"A": ("Speed", False), "B": ("Security", True), "C": ("Storage", False), "D": ("Editing", False)}, "Protection from threats.", "Firewall provides security."),
    ("What does PDF stand for?", {"A": ("Portable Document Format", True), "B": ("Personal Data File", False), "C": ("Public Document Format", False), "D": ("Printed Data File", False)}, "Same on any device.", "PDF is Portable Document Format."),
    ("Which is email service?", {"A": ("Instagram", False), "B": ("Gmail", True), "C": ("Twitter", False), "D": ("TikTok", False)}, "By Google.", "Gmail is email service."),
    ("Purpose of web browser?", {"A": ("Edit photos", False), "B": ("Access websites", True), "C": ("Play games", False), "D": ("Write code", False)}, "You're using one now.", "Browser accesses websites."),
    ("What does USB stand for?", {"A": ("Universal Serial Bus", True), "B": ("United System Board", False), "C": ("Universal System Bus", False), "D": ("Unified Serial Board", False)}, "Common port.", "USB is Universal Serial Bus.")
]

TECHNOLOGY_MEDIUM = [
    ("What is an IP address?", {"A": ("Internet Protocol address", True), "B": ("Internal Processing address", False), "C": ("Internet Provider address", False), "D": ("Internal Protocol address", False)}, "Unique identifier for devices.", "IP address identifies devices on network."),
    ("What is cloud computing?", {"A": ("Weather prediction", False), "B": ("Remote servers for storage", True), "C": ("Local storage", False), "D": ("Wireless connection", False)}, "Data stored remotely.", "Cloud computing uses remote servers."),
    ("What is open source software?", {"A": ("Free to use and modify", True), "B": ("Expensive software", False), "C": ("Closed code", False), "D": ("Windows only", False)}, "Source code is available.", "Open source allows code modification."),
    ("What is encryption?", {"A": ("Data compression", False), "B": ("Data security", True), "C": ("Data deletion", False), "D": ("Data backup", False)}, "Protects information.", "Encryption secures data."),
    ("What is a database?", {"A": ("Organized data collection", True), "B": ("Random files", False), "C": ("Image gallery", False), "D": ("Video player", False)}, "Structured information storage.", "Database stores organized data."),
    ("What is API?", {"A": ("Application Programming Interface", True), "B": ("Advanced Program Integration", False), "C": ("Automated Process Interface", False), "D": ("Application Process Integration", False)}, "Software communication.", "API enables software interaction."),
    ("What is bandwidth?", {"A": ("Data transfer capacity", True), "B": ("Storage space", False), "C": ("Processing speed", False), "D": ("Screen size", False)}, "Network capacity.", "Bandwidth is data transfer rate."),
    ("What is malware?", {"A": ("Malicious software", True), "B": ("Mail software", False), "C": ("Male software", False), "D": ("Main software", False)}, "Harmful programs.", "Malware is malicious software."),
    ("What is a cookie in web?", {"A": ("Small data file", True), "B": ("Snack", False), "C": ("Image file", False), "D": ("Video file", False)}, "Stores user data.", "Cookie stores website data."),
    ("What is VPN?", {"A": ("Virtual Private Network", True), "B": ("Very Private Network", False), "C": ("Visual Private Network", False), "D": ("Virtual Public Network", False)}, "Secure connection.", "VPN creates secure network."),
    ("What is cache?", {"A": ("Temporary storage", True), "B": ("Permanent storage", False), "C": ("Deleted files", False), "D": ("Backup files", False)}, "Speeds up access.", "Cache stores temporary data."),
    ("What is phishing?", {"A": ("Fraudulent attempt", True), "B": ("Fishing online", False), "C": ("Photo editing", False), "D": ("File sharing", False)}, "Stealing information.", "Phishing steals sensitive data."),
    ("What is algorithm?", {"A": ("Step-by-step procedure", True), "B": ("Random process", False), "C": ("Hardware component", False), "D": ("Software bug", False)}, "Problem-solving steps.", "Algorithm is systematic procedure."),
    ("What is debugging?", {"A": ("Finding and fixing errors", True), "B": ("Deleting bugs", False), "C": ("Creating bugs", False), "D": ("Ignoring errors", False)}, "Error correction.", "Debugging fixes code errors."),
    ("What is bandwidth throttling?", {"A": ("Limiting data speed", True), "B": ("Increasing speed", False), "C": ("Deleting data", False), "D": ("Storing data", False)}, "ISP speed control.", "Throttling limits bandwidth.")
]

TECHNOLOGY_HARD = [
    ("What is blockchain?", {"A": ("Distributed ledger", True), "B": ("Chain of blocks", False), "C": ("Database type", False), "D": ("Encryption method", False)}, "Decentralized record.", "Blockchain is distributed ledger technology."),
    ("What is machine learning?", {"A": ("AI subset", True), "B": ("Hardware learning", False), "C": ("Manual programming", False), "D": ("Computer repair", False)}, "Computers learn from data.", "Machine learning is AI that learns from data."),
    ("What is quantum computing?", {"A": ("Uses quantum mechanics", True), "B": ("Very fast PC", False), "C": ("Cloud computing", False), "D": ("Mobile computing", False)}, "Quantum bits.", "Quantum computing uses qubits."),
    ("What is containerization?", {"A": ("Application isolation", True), "B": ("Data compression", False), "C": ("File storage", False), "D": ("Network security", False)}, "Docker uses this.", "Containerization isolates applications."),
    ("What is microservices architecture?", {"A": ("Small independent services", True), "B": ("Tiny computers", False), "C": ("Small files", False), "D": ("Mini programs", False)}, "Modular design.", "Microservices are independent components."),
    ("What is edge computing?", {"A": ("Processing near data source", True), "B": ("Cloud computing", False), "C": ("Border security", False), "D": ("Screen edges", False)}, "Reduces latency.", "Edge computing processes data locally."),
    ("What is neural network?", {"A": ("AI model inspired by brain", True), "B": ("Computer network", False), "C": ("Internet connection", False), "D": ("Social network", False)}, "Mimics neurons.", "Neural networks model brain structure."),
    ("What is DevOps?", {"A": ("Development and Operations", True), "B": ("Device Operations", False), "C": ("Developer Options", False), "D": ("Device Optimization", False)}, "Combines dev and ops.", "DevOps integrates development and operations."),
    ("What is REST API?", {"A": ("Representational State Transfer", True), "B": ("Remote State Transfer", False), "C": ("Restful Application", False), "D": ("Resource State Transfer", False)}, "Web service architecture.", "REST is architectural style for APIs."),
    ("What is Big Data?", {"A": ("Extremely large datasets", True), "B": ("Large files", False), "C": ("Big storage", False), "D": ("Large programs", False)}, "Volume, velocity, variety.", "Big Data refers to massive datasets."),
    ("What is IoT?", {"A": ("Internet of Things", True), "B": ("Internet of Technology", False), "C": ("Internal of Things", False), "D": ("Internet of Thoughts", False)}, "Connected devices.", "IoT connects physical devices."),
    ("What is serverless computing?", {"A": ("Cloud provider manages servers", True), "B": ("No servers used", False), "C": ("Local servers", False), "D": ("Server-free internet", False)}, "Backend as service.", "Serverless abstracts server management."),
    ("What is GraphQL?", {"A": ("Query language for APIs", True), "B": ("Graph database", False), "C": ("Graphics language", False), "D": ("Google Query Language", False)}, "Alternative to REST.", "GraphQL queries APIs efficiently."),
    ("What is Kubernetes?", {"A": ("Container orchestration", True), "B": ("Programming language", False), "C": ("Database system", False), "D": ("Operating system", False)}, "Manages containers.", "Kubernetes orchestrates containers."),
    ("What is CI/CD?", {"A": ("Continuous Integration/Deployment", True), "B": ("Computer Integration", False), "C": ("Code Integration", False), "D": ("Central Integration", False)}, "Automated pipeline.", "CI/CD automates software delivery.")
]


SCIENCE_EASY = [
    ("What is H2O?", {"A": ("Water", True), "B": ("Hydrogen", False), "C": ("Oxygen", False), "D": ("Helium", False)}, "Two hydrogen, one oxygen.", "H2O is water molecule."),
    ("What planet is closest to Sun?", {"A": ("Venus", False), "B": ("Mercury", True), "C": ("Earth", False), "D": ("Mars", False)}, "First planet.", "Mercury is closest to Sun."),
    ("What is photosynthesis?", {"A": ("Plants make food", True), "B": ("Animals eat", False), "C": ("Water cycle", False), "D": ("Rock formation", False)}, "Plants use sunlight.", "Photosynthesis converts light to energy."),
    ("How many bones in human body?", {"A": ("206", True), "B": ("106", False), "C": ("306", False), "D": ("406", False)}, "Over 200.", "Humans have 206 bones."),
    ("What is gravity?", {"A": ("Force pulling objects", True), "B": ("Pushing force", False), "C": ("Light force", False), "D": ("Sound force", False)}, "Keeps us grounded.", "Gravity pulls objects together."),
    ("What is DNA?", {"A": ("Genetic material", True), "B": ("Protein", False), "C": ("Vitamin", False), "D": ("Mineral", False)}, "Carries genetic info.", "DNA stores genetic information."),
    ("What is evaporation?", {"A": ("Liquid to gas", True), "B": ("Gas to liquid", False), "C": ("Solid to liquid", False), "D": ("Liquid to solid", False)}, "Water becomes vapor.", "Evaporation changes liquid to gas."),
    ("What is the largest organ?", {"A": ("Skin", True), "B": ("Heart", False), "C": ("Liver", False), "D": ("Brain", False)}, "Covers your body.", "Skin is largest organ."),
    ("What causes seasons?", {"A": ("Earth's tilt", True), "B": ("Distance from Sun", False), "C": ("Moon phases", False), "D": ("Ocean currents", False)}, "Axis angle.", "Earth's tilt causes seasons."),
    ("What is oxygen symbol?", {"A": ("O", True), "B": ("Ox", False), "C": ("O2", False), "D": ("Og", False)}, "Single letter.", "Oxygen symbol is O."),
    ("What is speed of light?", {"A": ("300,000 km/s", True), "B": ("150,000 km/s", False), "C": ("450,000 km/s", False), "D": ("600,000 km/s", False)}, "Very fast.", "Light travels 300,000 km/s."),
    ("What is cell?", {"A": ("Basic unit of life", True), "B": ("Battery", False), "C": ("Prison room", False), "D": ("Phone", False)}, "Building block.", "Cell is life's basic unit."),
    ("What is atom?", {"A": ("Smallest unit of element", True), "B": ("Molecule", False), "C": ("Cell", False), "D": ("Particle", False)}, "Tiny particle.", "Atom is smallest element unit."),
    ("What is ecosystem?", {"A": ("Living and non-living interact", True), "B": ("Only animals", False), "C": ("Only plants", False), "D": ("Only water", False)}, "Environment system.", "Ecosystem includes all interactions."),
    ("What is metamorphosis?", {"A": ("Life cycle change", True), "B": ("Rock change", False), "C": ("Weather change", False), "D": ("Color change", False)}, "Butterfly transformation.", "Metamorphosis is life stage change.")
]

SCIENCE_MEDIUM = [
    ("What is mitochondria?", {"A": ("Cell powerhouse", True), "B": ("Cell wall", False), "C": ("Cell nucleus", False), "D": ("Cell membrane", False)}, "Produces energy.", "Mitochondria generates ATP."),
    ("What is Newton's first law?", {"A": ("Object in motion stays in motion", True), "B": ("Force equals mass times acceleration", False), "C": ("Action-reaction", False), "D": ("Gravity law", False)}, "Inertia.", "First law describes inertia."),
    ("What is pH scale?", {"A": ("Acidity measure", True), "B": ("Temperature scale", False), "C": ("Pressure measure", False), "D": ("Volume measure", False)}, "0-14 range.", "pH measures acidity/alkalinity."),
    ("What is periodic table?", {"A": ("Element organization", True), "B": ("Time table", False), "C": ("Calendar", False), "D": ("Schedule", False)}, "Chemical elements.", "Periodic table organizes elements."),
    ("What is enzyme?", {"A": ("Biological catalyst", True), "B": ("Vitamin", False), "C": ("Mineral", False), "D": ("Hormone", False)}, "Speeds reactions.", "Enzymes catalyze reactions."),
    ("What is osmosis?", {"A": ("Water movement through membrane", True), "B": ("Gas diffusion", False), "C": ("Solid dissolution", False), "D": ("Heat transfer", False)}, "Concentration gradient.", "Osmosis moves water across membranes."),
    ("What is electromagnetic spectrum?", {"A": ("Range of radiation", True), "B": ("Color range", False), "C": ("Sound range", False), "D": ("Temperature range", False)}, "Includes visible light.", "EM spectrum includes all radiation."),
    ("What is kinetic energy?", {"A": ("Energy of motion", True), "B": ("Stored energy", False), "C": ("Heat energy", False), "D": ("Light energy", False)}, "Moving objects.", "Kinetic energy is motion energy."),
    ("What is chromosome?", {"A": ("DNA structure", True), "B": ("Protein", False), "C": ("Cell part", False), "D": ("Organ", False)}, "Contains genes.", "Chromosomes carry genetic info."),
    ("What is catalyst?", {"A": ("Speeds reaction", True), "B": ("Slows reaction", False), "C": ("Stops reaction", False), "D": ("Starts reaction", False)}, "Not consumed.", "Catalyst accelerates reactions."),
    ("What is refraction?", {"A": ("Light bending", True), "B": ("Light reflection", False), "C": ("Light absorption", False), "D": ("Light emission", False)}, "Through different mediums.", "Refraction bends light."),
    ("What is homeostasis?", {"A": ("Body balance", True), "B": ("Cell division", False), "C": ("Energy production", False), "D": ("Waste removal", False)}, "Stable internal state.", "Homeostasis maintains equilibrium."),
    ("What is covalent bond?", {"A": ("Atoms share electrons", True), "B": ("Atoms transfer electrons", False), "C": ("Atoms lose electrons", False), "D": ("Atoms gain electrons", False)}, "Electron sharing.", "Covalent bonds share electrons."),
    ("What is natural selection?", {"A": ("Survival of fittest", True), "B": ("Random selection", False), "C": ("Human selection", False), "D": ("Artificial selection", False)}, "Darwin's theory.", "Natural selection drives evolution."),
    ("What is convection?", {"A": ("Heat transfer by fluid", True), "B": ("Heat by contact", False), "C": ("Heat by radiation", False), "D": ("Heat by conduction", False)}, "Fluid movement.", "Convection transfers heat via fluids.")
]

SCIENCE_HARD = [
    ("What is Heisenberg principle?", {"A": ("Uncertainty in measurement", True), "B": ("Energy conservation", False), "C": ("Mass-energy equivalence", False), "D": ("Relativity", False)}, "Quantum mechanics.", "Heisenberg uncertainty principle."),
    ("What is entropy?", {"A": ("Disorder measure", True), "B": ("Energy measure", False), "C": ("Temperature measure", False), "D": ("Pressure measure", False)}, "Thermodynamics.", "Entropy measures disorder."),
    ("What is CRISPR?", {"A": ("Gene editing tool", True), "B": ("Protein", False), "C": ("Virus", False), "D": ("Bacteria", False)}, "Genetic engineering.", "CRISPR edits genes."),
    ("What is quantum entanglement?", {"A": ("Particle correlation", True), "B": ("Particle collision", False), "C": ("Particle decay", False), "D": ("Particle fusion", False)}, "Spooky action.", "Entanglement links particles."),
    ("What is telomere?", {"A": ("Chromosome end", True), "B": ("Cell center", False), "C": ("DNA start", False), "D": ("Gene middle", False)}, "Aging marker.", "Telomeres protect chromosomes."),
    ("What is dark matter?", {"A": ("Invisible matter", True), "B": ("Black holes", False), "C": ("Dark energy", False), "D": ("Antimatter", False)}, "Most of universe.", "Dark matter is invisible mass."),
    ("What is superconductivity?", {"A": ("Zero resistance", True), "B": ("High resistance", False), "C": ("Variable resistance", False), "D": ("Negative resistance", False)}, "Very cold.", "Superconductors have no resistance."),
    ("What is stem cell?", {"A": ("Undifferentiated cell", True), "B": ("Plant cell", False), "C": ("Nerve cell", False), "D": ("Blood cell", False)}, "Can become any cell.", "Stem cells are pluripotent."),
    ("What is Doppler effect?", {"A": ("Frequency change", True), "B": ("Amplitude change", False), "C": ("Wavelength constant", False), "D": ("Speed change", False)}, "Moving source.", "Doppler shifts frequency."),
    ("What is RNA interference?", {"A": ("Gene silencing", True), "B": ("Protein synthesis", False), "C": ("DNA replication", False), "D": ("Cell division", False)}, "Regulatory mechanism.", "RNAi silences genes."),
    ("What is Higgs boson?", {"A": ("Mass-giving particle", True), "B": ("Energy particle", False), "C": ("Light particle", False), "D": ("Force particle", False)}, "God particle.", "Higgs gives mass."),
    ("What is apoptosis?", {"A": ("Programmed cell death", True), "B": ("Cell growth", False), "C": ("Cell division", False), "D": ("Cell mutation", False)}, "Controlled death.", "Apoptosis is planned cell death."),
    ("What is redox reaction?", {"A": ("Electron transfer", True), "B": ("Proton transfer", False), "C": ("Neutron transfer", False), "D": ("Atom transfer", False)}, "Oxidation-reduction.", "Redox involves electron exchange."),
    ("What is epigenetics?", {"A": ("Gene expression changes", True), "B": ("DNA sequence changes", False), "C": ("Protein changes", False), "D": ("Cell changes", False)}, "Beyond genetics.", "Epigenetics modifies gene activity."),
    ("What is antimatter?", {"A": ("Opposite charge particles", True), "B": ("Dark matter", False), "C": ("Negative matter", False), "D": ("Empty space", False)}, "Annihilates matter.", "Antimatter has opposite charge.")
]


GEOGRAPHY_EASY = [
    ("What is capital of France?", {"A": ("Paris", True), "B": ("London", False), "C": ("Berlin", False), "D": ("Rome", False)}, "City of lights.", "Paris is France's capital."),
    ("Which is largest ocean?", {"A": ("Pacific", True), "B": ("Atlantic", False), "C": ("Indian", False), "D": ("Arctic", False)}, "Biggest body of water.", "Pacific is largest ocean."),
    ("How many continents?", {"A": ("7", True), "B": ("5", False), "C": ("6", False), "D": ("8", False)}, "Count them all.", "There are 7 continents."),
    ("What is longest river?", {"A": ("Nile", True), "B": ("Amazon", False), "C": ("Yangtze", False), "D": ("Mississippi", False)}, "In Africa.", "Nile is longest river."),
    ("Which country has most people?", {"A": ("China", True), "B": ("India", False), "C": ("USA", False), "D": ("Indonesia", False)}, "Asian country.", "China has most population."),
    ("What is capital of Japan?", {"A": ("Tokyo", True), "B": ("Beijing", False), "C": ("Seoul", False), "D": ("Bangkok", False)}, "Largest city.", "Tokyo is Japan's capital."),
    ("Which is smallest continent?", {"A": ("Australia", True), "B": ("Europe", False), "C": ("Antarctica", False), "D": ("South America", False)}, "Island continent.", "Australia is smallest."),
    ("What is tallest mountain?", {"A": ("Everest", True), "B": ("K2", False), "C": ("Kilimanjaro", False), "D": ("Denali", False)}, "In Himalayas.", "Everest is tallest."),
    ("Which ocean is coldest?", {"A": ("Arctic", True), "B": ("Atlantic", False), "C": ("Pacific", False), "D": ("Indian", False)}, "Near North Pole.", "Arctic is coldest."),
    ("What is capital of Italy?", {"A": ("Rome", True), "B": ("Milan", False), "C": ("Venice", False), "D": ("Florence", False)}, "Ancient city.", "Rome is Italy's capital."),
    ("Which is largest desert?", {"A": ("Sahara", True), "B": ("Gobi", False), "C": ("Arabian", False), "D": ("Kalahari", False)}, "In Africa.", "Sahara is largest hot desert."),
    ("What is capital of USA?", {"A": ("Washington DC", True), "B": ("New York", False), "C": ("Los Angeles", False), "D": ("Chicago", False)}, "Not largest city.", "Washington DC is capital."),
    ("Which country is largest?", {"A": ("Russia", True), "B": ("Canada", False), "C": ("China", False), "D": ("USA", False)}, "Spans two continents.", "Russia is largest country."),
    ("What is Great Barrier Reef?", {"A": ("Coral reef", True), "B": ("Mountain range", False), "C": ("Desert", False), "D": ("Forest", False)}, "In Australia.", "Great Barrier Reef is coral."),
    ("Which is longest mountain range?", {"A": ("Andes", True), "B": ("Rockies", False), "C": ("Himalayas", False), "D": ("Alps", False)}, "In South America.", "Andes is longest range.")
]

GEOGRAPHY_MEDIUM = [
    ("What is Ring of Fire?", {"A": ("Volcanic belt", True), "B": ("Desert", False), "C": ("Ocean current", False), "D": ("Mountain range", False)}, "Pacific region.", "Ring of Fire has volcanoes."),
    ("What causes tides?", {"A": ("Moon's gravity", True), "B": ("Wind", False), "C": ("Earth's rotation", False), "D": ("Sun's heat", False)}, "Celestial body.", "Moon causes tides."),
    ("What is tundra?", {"A": ("Cold treeless region", True), "B": ("Hot desert", False), "C": ("Tropical forest", False), "D": ("Grassland", False)}, "Arctic climate.", "Tundra is cold biome."),
    ("What is equator?", {"A": ("0° latitude", True), "B": ("0° longitude", False), "C": ("Tropic line", False), "D": ("Polar circle", False)}, "Divides hemispheres.", "Equator is 0° latitude."),
    ("What is fjord?", {"A": ("Glacial valley", True), "B": ("Mountain peak", False), "C": ("Desert oasis", False), "D": ("River delta", False)}, "In Norway.", "Fjord is glacial inlet."),
    ("What is monsoon?", {"A": ("Seasonal wind", True), "B": ("Hurricane", False), "C": ("Tornado", False), "D": ("Blizzard", False)}, "In Asia.", "Monsoon is seasonal rain."),
    ("What is archipelago?", {"A": ("Island group", True), "B": ("Peninsula", False), "C": ("Isthmus", False), "D": ("Cape", False)}, "Multiple islands.", "Archipelago is island chain."),
    ("What is Prime Meridian?", {"A": ("0° longitude", True), "B": ("0° latitude", False), "C": ("Equator", False), "D": ("Tropic", False)}, "Through Greenwich.", "Prime Meridian is 0° longitude."),
    ("What is savanna?", {"A": ("Tropical grassland", True), "B": ("Desert", False), "C": ("Forest", False), "D": ("Tundra", False)}, "In Africa.", "Savanna is grassland."),
    ("What is isthmus?", {"A": ("Narrow land strip", True), "B": ("Wide plain", False), "C": ("Mountain range", False), "D": ("River valley", False)}, "Connects land masses.", "Isthmus is land bridge."),
    ("What is delta?", {"A": ("River mouth", True), "B": ("Mountain top", False), "C": ("Ocean trench", False), "D": ("Desert dune", False)}, "Sediment deposit.", "Delta is river mouth."),
    ("What is taiga?", {"A": ("Boreal forest", True), "B": ("Tropical forest", False), "C": ("Desert", False), "D": ("Grassland", False)}, "Coniferous trees.", "Taiga is northern forest."),
    ("What is plateau?", {"A": ("Elevated flatland", True), "B": ("Valley", False), "C": ("Mountain peak", False), "D": ("Canyon", False)}, "High flat area.", "Plateau is elevated plain."),
    ("What is strait?", {"A": ("Narrow water passage", True), "B": ("Wide ocean", False), "C": ("Deep trench", False), "D": ("Shallow bay", False)}, "Connects water bodies.", "Strait is water passage."),
    ("What is atoll?", {"A": ("Coral island", True), "B": ("Volcanic island", False), "C": ("Continental island", False), "D": ("Artificial island", False)}, "Ring-shaped.", "Atoll is coral ring.")
]

GEOGRAPHY_HARD = [
    ("What is Pangaea?", {"A": ("Ancient supercontinent", True), "B": ("Current continent", False), "C": ("Ocean", False), "D": ("Mountain", False)}, "All land together.", "Pangaea was supercontinent."),
    ("What is subduction zone?", {"A": ("Tectonic plate collision", True), "B": ("Earthquake zone", False), "C": ("Volcanic zone", False), "D": ("Fault line", False)}, "Plate goes under.", "Subduction is plate diving."),
    ("What is karst topography?", {"A": ("Limestone landscape", True), "B": ("Volcanic landscape", False), "C": ("Glacial landscape", False), "D": ("Desert landscape", False)}, "Caves and sinkholes.", "Karst has dissolved rock."),
    ("What is antipode?", {"A": ("Opposite side of Earth", True), "B": ("North Pole", False), "C": ("South Pole", False), "D": ("Equator", False)}, "Diametrically opposite.", "Antipode is Earth's opposite."),
    ("What is moraine?", {"A": ("Glacial deposit", True), "B": ("River deposit", False), "C": ("Wind deposit", False), "D": ("Ocean deposit", False)}, "Glacier leaves it.", "Moraine is glacial debris."),
    ("What is orographic lift?", {"A": ("Mountain air rise", True), "B": ("Valley wind", False), "C": ("Ocean breeze", False), "D": ("Desert wind", False)}, "Causes rain.", "Orographic lift creates precipitation."),
    ("What is rift valley?", {"A": ("Tectonic separation", True), "B": ("River valley", False), "C": ("Glacial valley", False), "D": ("Erosion valley", False)}, "Plates pull apart.", "Rift valley from divergence."),
    ("What is thermocline?", {"A": ("Ocean temperature layer", True), "B": ("Atmospheric layer", False), "C": ("Earth's core layer", False), "D": ("Ice layer", False)}, "Water temperature change.", "Thermocline is temp gradient."),
    ("What is drumlin?", {"A": ("Glacial hill", True), "B": ("Sand dune", False), "C": ("Volcanic cone", False), "D": ("River terrace", False)}, "Elongated hill.", "Drumlin is glacial formation."),
    ("What is halocline?", {"A": ("Salinity gradient", True), "B": ("Temperature gradient", False), "C": ("Pressure gradient", False), "D": ("Density gradient", False)}, "Salt concentration change.", "Halocline is salinity layer."),
    ("What is esker?", {"A": ("Glacial ridge", True), "B": ("River bank", False), "C": ("Mountain ridge", False), "D": ("Sand bar", False)}, "Winding ridge.", "Esker is glacial deposit."),
    ("What is badlands?", {"A": ("Eroded terrain", True), "B": ("Fertile land", False), "C": ("Forest land", False), "D": ("Wetland", False)}, "Heavily eroded.", "Badlands are eroded areas."),
    ("What is guyot?", {"A": ("Flat-topped seamount", True), "B": ("Coral reef", False), "C": ("Ocean trench", False), "D": ("Volcanic island", False)}, "Underwater mountain.", "Guyot is submerged volcano."),
    ("What is loess?", {"A": ("Wind-blown silt", True), "B": ("River sediment", False), "C": ("Volcanic ash", False), "D": ("Glacial till", False)}, "Fine sediment.", "Loess is wind deposit."),
    ("What is pingo?", {"A": ("Ice-cored hill", True), "B": ("Sand dune", False), "C": ("Volcanic cone", False), "D": ("Coral mound", False)}, "In permafrost.", "Pingo is ice hill.")
]

GENERAL_EASY = [
    ("Who painted Mona Lisa?", {"A": ("Leonardo da Vinci", True), "B": ("Michelangelo", False), "C": ("Picasso", False), "D": ("Van Gogh", False)}, "Renaissance artist.", "Da Vinci painted Mona Lisa."),
    ("What year did WWII end?", {"A": ("1945", True), "B": ("1944", False), "C": ("1946", False), "D": ("1943", False)}, "Mid-1940s.", "WWII ended in 1945."),
    ("Who wrote Romeo and Juliet?", {"A": ("Shakespeare", True), "B": ("Dickens", False), "C": ("Austen", False), "D": ("Hemingway", False)}, "English playwright.", "Shakespeare wrote it."),
    ("What is currency of Japan?", {"A": ("Yen", True), "B": ("Yuan", False), "C": ("Won", False), "D": ("Rupee", False)}, "Japanese money.", "Yen is Japan's currency."),
    ("Who was first US president?", {"A": ("George Washington", True), "B": ("Thomas Jefferson", False), "C": ("Abraham Lincoln", False), "D": ("John Adams", False)}, "Founding father.", "Washington was first."),
    ("What is Eiffel Tower made of?", {"A": ("Iron", True), "B": ("Steel", False), "C": ("Bronze", False), "D": ("Copper", False)}, "Metal structure.", "Eiffel Tower is iron."),
    ("Who invented telephone?", {"A": ("Alexander Graham Bell", True), "B": ("Thomas Edison", False), "C": ("Nikola Tesla", False), "D": ("Marconi", False)}, "Scottish inventor.", "Bell invented telephone."),
    ("What is Olympic symbol?", {"A": ("Five rings", True), "B": ("Torch", False), "C": ("Medal", False), "D": ("Flag", False)}, "Interlocking circles.", "Five rings represent Olympics."),
    ("Who wrote Harry Potter?", {"A": ("J.K. Rowling", True), "B": ("J.R.R. Tolkien", False), "C": ("C.S. Lewis", False), "D": ("Roald Dahl", False)}, "British author.", "Rowling wrote Harry Potter."),
    ("What is Statue of Liberty holding?", {"A": ("Torch", True), "B": ("Book", False), "C": ("Sword", False), "D": ("Flag", False)}, "In right hand.", "Liberty holds torch."),
    ("Who discovered America?", {"A": ("Christopher Columbus", True), "B": ("Amerigo Vespucci", False), "C": ("Leif Erikson", False), "D": ("Marco Polo", False)}, "1492 voyage.", "Columbus discovered America."),
    ("What is Big Ben?", {"A": ("Clock tower", True), "B": ("Bridge", False), "C": ("Palace", False), "D": ("Museum", False)}, "In London.", "Big Ben is clock tower."),
    ("Who painted Starry Night?", {"A": ("Van Gogh", True), "B": ("Monet", False), "C": ("Picasso", False), "D": ("Rembrandt", False)}, "Dutch artist.", "Van Gogh painted it."),
    ("What is Taj Mahal?", {"A": ("Mausoleum", True), "B": ("Palace", False), "C": ("Temple", False), "D": ("Fort", False)}, "In India.", "Taj Mahal is tomb."),
    ("Who invented light bulb?", {"A": ("Thomas Edison", True), "B": ("Nikola Tesla", False), "C": ("Benjamin Franklin", False), "D": ("Alexander Bell", False)}, "American inventor.", "Edison invented bulb.")
]

GENERAL_MEDIUM = [
    ("What is Renaissance?", {"A": ("Cultural rebirth", True), "B": ("War period", False), "C": ("Industrial era", False), "D": ("Dark ages", False)}, "14th-17th century.", "Renaissance was cultural revival."),
    ("Who wrote 1984?", {"A": ("George Orwell", True), "B": ("Aldous Huxley", False), "C": ("Ray Bradbury", False), "D": ("H.G. Wells", False)}, "Dystopian novel.", "Orwell wrote 1984."),
    ("What is Magna Carta?", {"A": ("Charter of rights", True), "B": ("Declaration", False), "C": ("Treaty", False), "D": ("Constitution", False)}, "1215 document.", "Magna Carta limited power."),
    ("Who composed Moonlight Sonata?", {"A": ("Beethoven", True), "B": ("Mozart", False), "C": ("Bach", False), "D": ("Chopin", False)}, "German composer.", "Beethoven composed it."),
    ("What is Cold War?", {"A": ("Political tension", True), "B": ("Actual war", False), "C": ("Trade war", False), "D": ("Civil war", False)}, "USA vs USSR.", "Cold War was ideological conflict."),
    ("Who painted The Scream?", {"A": ("Edvard Munch", True), "B": ("Van Gogh", False), "C": ("Picasso", False), "D": ("Dali", False)}, "Norwegian artist.", "Munch painted The Scream."),
    ("What is Rosetta Stone?", {"A": ("Ancient decree", True), "B": ("Precious gem", False), "C": ("Building", False), "D": ("Weapon", False)}, "Helped decode hieroglyphs.", "Rosetta Stone is ancient text."),
    ("Who was Cleopatra?", {"A": ("Egyptian queen", True), "B": ("Greek goddess", False), "C": ("Roman empress", False), "D": ("Persian princess", False)}, "Last pharaoh.", "Cleopatra ruled Egypt."),
    ("What is Silk Road?", {"A": ("Trade route", True), "B": ("Actual road", False), "C": ("River", False), "D": ("Mountain pass", False)}, "Connected East-West.", "Silk Road was trade network."),
    ("Who wrote The Odyssey?", {"A": ("Homer", True), "B": ("Virgil", False), "C": ("Sophocles", False), "D": ("Euripides", False)}, "Ancient Greek poet.", "Homer wrote The Odyssey."),
    ("What is Bastille Day?", {"A": ("French national day", True), "B": ("British holiday", False), "C": ("American holiday", False), "D": ("German holiday", False)}, "July 14.", "Bastille Day celebrates revolution."),
    ("Who was Genghis Khan?", {"A": ("Mongol emperor", True), "B": ("Chinese emperor", False), "C": ("Japanese shogun", False), "D": ("Indian king", False)}, "Founded empire.", "Genghis Khan ruled Mongols."),
    ("What is Parthenon?", {"A": ("Greek temple", True), "B": ("Roman colosseum", False), "C": ("Egyptian pyramid", False), "D": ("Mayan temple", False)}, "In Athens.", "Parthenon is ancient temple."),
    ("Who discovered penicillin?", {"A": ("Alexander Fleming", True), "B": ("Louis Pasteur", False), "C": ("Marie Curie", False), "D": ("Jonas Salk", False)}, "Scottish scientist.", "Fleming discovered penicillin."),
    ("What is Gutenberg's invention?", {"A": ("Printing press", True), "B": ("Telescope", False), "C": ("Compass", False), "D": ("Clock", False)}, "Revolutionized books.", "Gutenberg invented printing press.")
]

GENERAL_HARD = [
    ("What is Treaty of Westphalia?", {"A": ("Ended Thirty Years War", True), "B": ("Ended WWI", False), "C": ("Ended WWII", False), "D": ("Ended Cold War", False)}, "1648 peace.", "Westphalia ended religious war."),
    ("Who was Hammurabi?", {"A": ("Babylonian king", True), "B": ("Egyptian pharaoh", False), "C": ("Greek philosopher", False), "D": ("Roman emperor", False)}, "Created code of laws.", "Hammurabi made first laws."),
    ("What is Bayeux Tapestry?", {"A": ("Norman conquest record", True), "B": ("Religious artwork", False), "C": ("Royal portrait", False), "D": ("Battle map", False)}, "1066 embroidery.", "Bayeux shows Norman invasion."),
    ("Who was Akbar?", {"A": ("Mughal emperor", True), "B": ("Ottoman sultan", False), "C": ("Persian shah", False), "D": ("Chinese emperor", False)}, "Ruled India.", "Akbar was Mughal ruler."),
    ("What is Hagia Sophia?", {"A": ("Byzantine cathedral", True), "B": ("Roman temple", False), "C": ("Greek palace", False), "D": ("Ottoman mosque", False)}, "In Istanbul.", "Hagia Sophia was church."),
    ("Who wrote The Prince?", {"A": ("Machiavelli", True), "B": ("Dante", False), "C": ("Petrarch", False), "D": ("Boccaccio", False)}, "Political treatise.", "Machiavelli wrote The Prince."),
    ("What is Meiji Restoration?", {"A": ("Japanese modernization", True), "B": ("Chinese revolution", False), "C": ("Korean reform", False), "D": ("Thai transformation", False)}, "1868 reform.", "Meiji modernized Japan."),
    ("Who was Suleiman?", {"A": ("Ottoman sultan", True), "B": ("Persian shah", False), "C": ("Mughal emperor", False), "D": ("Arab caliph", False)}, "The Magnificent.", "Suleiman ruled Ottomans."),
    ("What is Domesday Book?", {"A": ("Medieval survey", True), "B": ("Religious text", False), "C": ("Legal code", False), "D": ("Historical chronicle", False)}, "1086 England.", "Domesday recorded land."),
    ("Who was Ashoka?", {"A": ("Indian emperor", True), "B": ("Chinese emperor", False), "C": ("Persian king", False), "D": ("Greek ruler", False)}, "Mauryan dynasty.", "Ashoka ruled ancient India."),
    ("What is Hanseatic League?", {"A": ("Medieval trade alliance", True), "B": ("Military alliance", False), "C": ("Religious order", False), "D": ("Political union", False)}, "Northern Europe.", "Hanseatic was trade group."),
    ("Who was Saladin?", {"A": ("Muslim sultan", True), "B": ("Christian king", False), "C": ("Mongol khan", False), "D": ("Byzantine emperor", False)}, "Fought Crusaders.", "Saladin led Muslims."),
    ("What is Cyrus Cylinder?", {"A": ("Ancient charter", True), "B": ("Weapon", False), "C": ("Building", False), "D": ("Coin", False)}, "Persian artifact.", "Cyrus Cylinder is ancient decree."),
    ("Who was Charlemagne?", {"A": ("Frankish emperor", True), "B": ("English king", False), "C": ("Spanish king", False), "D": ("Italian duke", False)}, "Holy Roman Emperor.", "Charlemagne united Europe."),
    ("What is Upanishads?", {"A": ("Hindu texts", True), "B": ("Buddhist texts", False), "C": ("Jain texts", False), "D": ("Sikh texts", False)}, "Ancient philosophy.", "Upanishads are Hindu scriptures.")
]
