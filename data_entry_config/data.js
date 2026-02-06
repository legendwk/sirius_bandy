// Team and player data for bandy match tracker

const TEAMS = {
    'iks': { full: 'IK Sirius', short: 'Sirius', abbr: 'IKS', color: '#4a7cb5', text: '#fff', logo: 'sirius logo.png' },
    'vet': { full: 'Vetlanda BK', short: 'Vetlanda', abbr: 'VBK', color: '#fff300', text: '#000', logo: 'vetlanda logo.png' },
    'villa': { full: 'Villa Lidköping BK', short: 'Villa', abbr: 'VLBK', color: '#2c2d84', text: '#fff', logo: 'villa logo.png' },
    'aik': { full: 'AIK Bandy', short: 'AIK', abbr: 'AIK', color: '#07294a', text: '#c9a227', logo: 'aik logo.png' },
    'bol': { full: 'Bollnäs GIF', short: 'Bollnäs', abbr: 'BGIF', color: '#0e3b52', text: '#f38755', logo: 'bollnas logo.png' },
    'bro': { full: 'Broberg/Söderhamn', short: 'Broberg', abbr: 'BRO', color: '#0074be', text: '#ffd520', logo: 'broberg logo.png' },
    'eds': { full: 'Edsbyns IF', short: 'Edsbyn', abbr: 'EIF', color: '#033863', text: '#e4b34e', logo: 'edsbyn logo.png' },
    'fri': { full: 'Frillesås Bandy', short: 'Frillesås', abbr: 'FBK', color: '#00864c', text: '#fede01', logo: 'frillesas logo.png' },
    'gri': { full: 'Gripen Trollhättan', short: 'Gripen', abbr: 'GBK', color: '#fedd01', text: '#000', logo: 'gripen logo.png' },
    'ham': { full: 'Hammarby IF', short: 'Hammarby', abbr: 'HIF', color: '#01a957', text: '#fff', logo: 'hammarby logo.png' },
    'mot': { full: 'IFK Motala', short: 'Motala', abbr: 'MOT', color: '#004a92', text: '#fff', logo: 'motala logo.png' },
    'saik': { full: 'Sandvikens AIK', short: 'Sandviken', abbr: 'SAIK', color: '#000', text: '#fff', logo: 'saik logo.png' },
    'vän': { full: 'IFK Vänersborg', short: 'Vänersborg', abbr: 'VÄN', color: '#005a9b', text: '#fff', logo: 'vanersborg logo.png' },
    'vsk': { full: 'Västerås SK', short: 'Västerås', abbr: 'VSK', color: '#018248', text: '#fff', logo: 'vsk logo.png' },
    'rät': { full: 'IFK Rättvik', short: 'Rättvik', abbr: 'IFKR', color: '#1f50a6', text: '#fff', logo: 'rattvik logo.png' },
    'aby': { full: 'ÅBY/TJUREDA IF', short: 'Åby Tjureda', abbr: 'AIF', color: '#ffdc00', text: '#000', logo: 'aby.png' },
    'bltc': { full: 'IF Boltic', short: 'Boltic', abbr: 'IFB', color: '#0a5eaf', text: '#fbe11f', logo: 'boltic-frilagd.png' },
    'möl': { full: 'Mölndal Bandy', short: 'Mölndal', abbr: 'MÖL', color: '#394ffb', text: '#fff', logo: 'mölndal.png' },
    'bois': { full: 'Uppsala BoIS', short: 'BoIS', abbr: 'BoIS', color: '#e4312b', text: '#ffed01', logo: 'bois.png' },
    'bltc': { full: 'Skirö AIK', short: 'Skirö', abbr: 'SAIK', color: '#01853e', text: '#015696', logo: 'skirö.png' }
};

// Players organized by team
// Each player has: number, name, image (optional)
const PLAYERS = {
    'iks': [
        { num: '13', name: 'Anton Andersson', image: 'anton.png' },
        { num: '80', name: 'Axel Götlin', image: 'axel.png' },
        { num: '12', name: 'Oscar Qvist', image: 'qvist.png' },
        { num: '15', name: 'Jerker Ortman', image: 'jerker.png' },
        { num: '40', name: 'Sune Gustafsson', image: 'sune.png' },
        // { num: '2', name: 'Stefan Kröller', image: 'kröller.png' },
        // { num: '6', name: 'David Thorén', image: 'davva.png' },
        { num: '61', name: 'Ted Haraldsson', image: 'harald.png' },
        // { num: '7', name: 'Jimmy Jansson', image: 'jimmy.jpg' },
        { num: '17', name: 'Nils Bergström', image: 'nisse.png' },
        { num: '39', name: 'Arvid Tapper', image: 'arvid.png' },
        // { num: '10', name: 'Ted Bergström', image: 'tedb.png' },
        { num: '11', name: 'Albin Thomsen', image: 'albin.png' },
        // { num: '20', name: 'Kalle Mårtensson', image: 'kalle.png' },
        { num: '70', name: 'Colin Dahlberg', image: 'colin.png' },
        { num: '66', name: 'Alexander Karlgren', image: 'karlgren.jpg' },
        { num: '97', name: 'Alexander Härndahl', image: 'harndahl.jpg' },
        // { num: '9', name: 'Emil Eskhult', image: 'emil.jpg' },
        { num: '7', name: 'Samuel Heeger', image: 'heeger.png' },
        // { num: '9', name: 'Emil Eskhult', image: 'emil.jpg' },
        { num: '3', name: 'Simon Blomqvist', image: 'simonblomqvist.png' },
        { num: '21', name: 'Svante Vessby', image: 'svantevessby.png' },
        { num: '29', name: 'Marcus Lindholm', image: 'marcuslindholm.png' },
        { num: '9', name: 'Johannes Camilton', image: 'johannescamilton.png' },
        { num: '8', name: 'Joel Forsberg', image: 'joelforsberg.png' }

    ],
    'vet': [
        { num: '1', name: 'Målvakt 1' },
        { num: '30', name: 'Målvakt 2' }
        // Add more Vetlanda players as needed
    ]
    // Add more teams as needed
};

// All events defined in one place
// id: internal identifier, label: display name, key: default keybinding, subevents: optional array
const EVENT_CONFIG = [
    { id: 'skott', label: 'Skott', key: 's', subevents: ['räddning', 'utanför', 'täckt'] },
    { id: 'mål', label: 'Mål', key: 'g', subevents: ['spelmål', 'hörnmål', 'straffmål', 'frislagsmål'] },
    {id: 'skottyp', label: 'Skottyp', key: 'w', subevents: ['friställande', 'inspel', 'utifrån', 'dribbling', 'centralt', 'fast', 'retur']},
    { id: 'närkamp', label: 'Närkamp', key: 'n' },
    { id: 'brytning', label: 'Brytning', key: 'b' },
    { id: 'bolltapp', label: 'Bolltapp', key: 't', subevents: ['tappad', 'passförsök'] },
    { id: 'passning', label: 'Passning', key: 'p', subevents: ['straffområde', 'lång', 'farlig'] },
    { id: 'frislag', label: 'Frislag', key: 'f' },
    { id: 'hörna', label: 'Hörna', key: 'c' },
    { id: 'straff', label: 'Straff', key: 'r' },
    { id: 'friläge', label: 'Friläge', key: 'l' },
    { id: 'inslag', label: 'Inslag', key: 'i' },
    { id: 'utkast', label: 'Utkast', key: 'u' },
    { id: 'avslag', label: 'Avslag', key: 'v' },
    { id: 'rensning', label: 'Rensning', key: 'e' },
    { id: 'offside', label: 'Offside', key: 'o' },
    { id: 'utvisning', label: 'Utvisning', key: 'x', subevents: ['5a', '10a'] },
    { id: 'kontring', label: 'Kontring', key: 'k' }
];

// Derived arrays for backwards compatibility
const EVENTS = EVENT_CONFIG.map(e => e.id);
const SUBEVENTS = Object.fromEntries(
    EVENT_CONFIG.filter(e => e.subevents).map(e => [e.id, e.subevents])
);

// Paths updated for main directory location
const LOGO_PATH = 'bilder/logos/';
const PLAYER_PATH = 'bilder/player_pics/';
