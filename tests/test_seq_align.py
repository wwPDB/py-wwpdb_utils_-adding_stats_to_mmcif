import unittest
from adding_stats_to_mmcif.pairwise_align import SequenceAlign

no_match = 'XXXXXXXXXX'

test_sequences = ['MEKLEVGIYTRAREGEIACGDACLVKRVEGVIFLAVGDGIGHGPEAARAAEIAIASMESSMNTGLVNIFQLCHRELRGTRGAVAALCRVDRRQGLWQAAIVGNIHVKILSAKGIITPLATPGILGYNYPHQLLIAKGSYQEGDLFLIHSDGIQEGAVPLALLANYRLTAEELVRLIGEKYGRRDDDVAVIVAR',
                'GGUCAAGAUGGUAAGGGCCCACGGUGGAUGCCUCGGCACCCGAGCCGAUGAAGGACGUGGCUACCUGCGAUAAGCCAGGGGGAGCCGGUAGCGGGCGUGGAUCCCUGGAUGUCCGAAUGGGGGAACCCGGCCGGCGGGAACGCCGGUCACCGCGCUUUUUGCGCGGGGGGAACCUGGGGAACUGAAACAUCUCAGUACCCAGAGGAGAGGAAAGAGAAAUCGACUCCCUGAGUAGCGGCGAGCGAAAGGGGACCAGCCUAAACCGUCCGGCUUGUCCGGGCGGGGUCGUGGGGCCCUCGGACACCGAAUCCCCAGCCUAGCCGAAGCUGUUGGGAAGCAGCGCCAGAGAGGGUGAAAGCCCCGUAGGCGAAAGGUGGGGGGAUAGGUGAGGGUACCCGAGUACCCCGUGGUUCGUGGAGCCAUGGGGGAAUCUGGGCGGACCACCGCCUAAGGCUAAGUACUCCGGGUGACCGAUAGCGCACCAGUACCGUGAGGGAAAGGUGAAAAGAACCCCGGGAGGGGAGUGAAAUAGAGCCUGAAACCGUGGGCUUACAAGCAGUCACGGCCCCGCAAGGGGUUGUGGCGUGCCUAUUGAAGCAUGAGCCGGCGACUCACGGUCGUGGGCGAGCUUAAGCCGUUGAGGCGGAGGCGUAGGGAAACCGAGUCCGAACAGGGCGCAAACGGCCCGCACGCGGGCCGAAAAGUCCGCGGCCGUGGACCCGAAACCGGGCGAGCUAGCCCUGGCCAGGGUGAAGCUGGGGUGAGACCCAGUGGAGGCCCGAACCGGUGGGGGAUGCAAACCCCUCGGAUGAGCUGGGGCUAGGAGUGAAAAGCUAACCGAGCCCGGAGAUAGCUGGUUCUCCCCGAAAUGACUUUAGGGUCAGCCUCAGGCGCUGACUGGGGCCUGUAGAGCACUGAUAGGGCUAGGGGGCCCACCAGCCUACCAAACCCUGUCAAACUCCGAAGGGUCCCAGGUGGAGCCUGGGAGUGAGGGCGCGAGCGAUAACGUCCGCGUCCGAGCGCGGGAACAACCGAGACCGCCAGCUAAGGCCCCCAAGUCUGGGCUAAGUGGUAAAGGAUGUGGCGCCGCGAAGACAGCCAGGAUGUUGGCUUAGAAGCAGCCAUCAUUUAAAGAGUGCGUAAUAGCUCACUGGUCGAGUGGCGCCGCGCCGAAAAUGAUCGGGGCUUAAGCCCAGCGCCGAAGCUGCGGGUCUGGGGGAUGACCCCAGGCGGUAGGGGAGCGUUCCCGAUGCCGAUGAAGGCCGACCCGCGAGGGCGGCUGGAGGUAAGGGAAGUGCGAAUGCCGGCAUGAGUAACGAUAAAGAGGGUGAGAAUCCCUCUCGCCGUAAGCCCAAGGGUUCCUACGCAAUGGUCGUCAGCGUAGGGUUAGGCGGGACCUAAGGUGAAGCCGAAAGGCGUAGCCGAAGGGCAGCCGGUUAAUAUUCCGGCCCUUCCCGCAGGUGCGAUGGGGGGACGCUCUAGGCUAGGGGGACCGGAGCCAUGGACGAGCCCGGCCAGAAGCGCAGGGUGGGAGGUAGGCAAAUCCGCCUCCCAACAAGCUCUGCGUGGUGGGGAAGCCCGUACGGGUGACAACCCCCCGAAGCCAGGGAGCCAAGAAAAGCCUCUAAGCACAACCUGCGGGAACCCGUACCGCAAACCGACACAGGUGGGCGGGUGCAAGAGCACUCAGGCGCGCGGGAGAACCCUCGCCAAGGAACUCUGCAAGUUGGCCCCGUAACUUCGGGAGAAGGGGUGCUCCCUGGGGUGAUGAGCCCCGGGGAGCCGCAGUGAACAGGCUCUGGCGACUGUUUACCAAAAACACAGCUCUCUGCGAACUCGUAAGAGGAGGUAUAGGGAGCGACGCUUGCCCGGUGCCGGAAGGUCAAGGGGAGGGGUGCAAGCCCCGAACCGAAGCCCCGGUGAACGGCGGCCGUAACUAUAACGGUCCUAAGGUAGCGAAAUUCCUUGUCGGGUAAGUUCCGACCUGCACGAAAAGCGUAACGACCGGAGCGCUGUCUCGGCGAGGGACCCGGUGAAAUUGAACUGGCCGUGAAGAUGCGGCCUACCCGUGGCAGGACGAAAAGACCCCGUGGAGCUUUACUGCAGCCUGGUGUUGGCUCUUGGUCGCGCCUGCGUAGGAUAGGUGGGAGCCUGUGAACCCCCGCCUCCGGGUGGGGGGGAGGCGCCGGUGAAAUACCACCCUGGCGCGGCUGGGGGCCUAACCCUCGGAUGGGGGGACAGCGCUUGGCGGGCAGUUUGACUGGGGCGGUCGCCUCCUAAAAGGUAACGGAGGCGCCCAAAGGUCCCCUCAGGCGGGACGGAAAUCCGCCGGAGAGCGCAAGGGUAGAAGGGGGCCUGACUGCGAGGCCUGCAAGCCGAGCAGGGGCGAAAGCCGGGCCUAGUGAACCGGUGGUCCCGUGUGGAAGGGCCAUCGAUCAACGGAUAAAAGUUACCCCGGGGAUAACAGGCUGAUCUCCCCCGAGCGUCCACAGCGGCGGGGAGGUUUGGCACCUCGAUGUCGGCUCGUCGCAUCCUGGGGCUGAAGAAGGUCCCAAGGGUUGGGCUGUUCGCCCAUUAAAGCGGCACGCGAGCUGGGUUCAGAACGUCGUGAGACAGUUCGGUCUCUAUCCGCCACGGGCGCAGGAGGCUUGAGGGGGGCUCUUCCUAGUACGAGAGGACCGGAAGGGACGCACCUCUGGUUUCCCAGCUGUCCCUCCAGGGGCAUAAGCUGGGUAGCCAUGUGCGGAAGGGAUAACCGCUGAAAGCAUCUAAGCGGGAAGCCCGCCCCAAGAUGAGGCCUCCCACGGCGUCAAGCCGGUAAGGACCCGGGAAGACCACCCGGUGGAUGGGCCGGGGGUGUAAGCGCCGCGAGGCGUUGAGCCGACCGGUCCCAAUCGUCCGAGGUCUUGACCCCUCC',
'MGDGGEGEDEVQFLRTDDEVVLQCSATVLKEQLKLCLAAEGFGNRLCFLEPTSNAQNVPPDLAICCFTLEQSLSVRALQEMLANTVEAGVESSQGGGHRTLLYGHAILLRHAHSRMYLSCLTTSRSMTDKLAFDVGLQEDATGEACWWTMHPASKQRSEGEKVRVGDDLILVSVSSERYLHLSTASGELQVDASFMQTLWNMNPICSCCEEGYVTGGHVLRLFHGHMDECLTISAADSDDQRRLVYYEGGAVCTHARSLWRLEPLRISWSGSHLRWGQPLRIRHVTTGRYLALTEDQGLVVVDACKAHTKATSFCFRVSKEKLDTAPKRDVEGMGPPEIKYGESLCFVQHVASGLWLTYAAPDPKALRLGVLKKKAILHQEGHMDDALFLTRCQQEESQAARMIHSTAGLYNQFIKGLDSFSGKPRGSGPPAGPALPIEAVILSLQDLIGYFEPPSEELQHEEKQSKLRSLRNRQSLFQEEGMLSLVLNCIDRLNVYTTAAHFAEYAGEEAAESWKEIVNLLYELLASLIRGNRANCALFSTNLDWVVSKLDRLEASSGILEVLYCVLIESPEVLNIIQENHIKSIISLLDKHGRNHKVLDVLCSLCVCNGVAVRSNQDLITENLLPGRELLLQTNLINYVTSIRPNIFVGRAEGSTQYGKWYFEVMVDEVVPFLTAQATHLRVGWALTEGYSPYPGGGEGWGGNGVGDDLYSYGFDGLHLWTGHVARPVTSPGQHLLAPEDVVSCCLDLSVPSISFRINGCPVQGVFEAFNLDGLFFPVVSFSAGVKVRFLLGGRHGEFKFLPPPGYAPCHEAVLPRERLRLEPIKEYRREGPRGPHLVGPSRCLSHTDFVPCPVDTVQIVLPPHLERIREKLAENIHELWALTRIEQGWTYGPVRDDNKRLHPCLVNFHSLPEPERNYNLQMSGETLKTLLALGCHVGMADEKAEDNLKKTKLPKTYMMSNGYKPAPLDLSHVRLTPAQTTLVDRLAENGHNVWARDRVAQGWSYSAVQDIPARRNPRLVPYRLLDEATKRSNRDSLCQAVRTLLGYGYNIEPPDQEPSQVENQSRWDRVRIFRAEKSYTVQSGRWYFEFEAVTTGEMRVGWARPELRPDVELGADELAYVFNGHRGQRWHLGSEPFGRPWQSGDVVGCMIDLTENTIIFTLNGEVLMSDSGSETAFREIEIGDGFLPVCSLGPGQVGHLNLGQDVSSLRFFAICGLQEGFEPFAINMQRPVTTWFSKSLPQFEPVPPEHPHYEVARMDGTVDTPPCLRLAHRTWGSQNSLVEMLFLRLSLPVQFHQHFRCTAGATPLAPPGLQPPAEDEARAAEPDPDYENLRRSAGGWGEAEGGKEGTAKEGTPGGTPQPGVEAQPVRAENEKDATTEKNKKRGFLFKAKKAAMMTQPPATPALPRLPHDVVPADNRDDPEIILNTTTYYYSVRVFAGQEPSCVWVGWVTPDYHQHDMNFDLSKVRAVTVTMGDEQGNVHSSLKCSNCYMVWGGDFVSPGQQGRISHTDLVIGCLVDLATGLMTFTANGKESNTFFQVEPNTKLFPAVFVLPTHQNVIQFELGKQKNIMPLSAAMFLSERKNPAPQCPPRLEVQMLMPVSWSRMPNHFLQVETRRAGERLGWAVQCQDPLTMMALHIPEENRCMDILELSERLDLQRFHSHTLRLYRAVCALGNNRVAHALCSHVDQAQLLHALEDAHLPGPLRAGYYDLLISIHLESACRSRRSMLSEYIVPLTPETRAITLFPPGRKGGNARRHGLPGVGVTTSLRPPHHFSPPCFVAALPAAGVAEAPARLSPAIPLEALRDKALRMLGEAVRDGGQHARDPVGGSVEFQFVPVLKLVSTLLVMGIFGDEDVKQILKMIEPEVFTEEEEEEEEEEEEEEEEEEDEEEKEEDEEEEEKEDAEKEEEEAPEGEKEDLEEGLLQMKLPESVKLQMCNLLEYFCDQELQHRVESLAAFAERYVDKLQANQRSRYALLMRAFTMSAAETARRTREFRSPPQEQINMLLHFKDEADEEDCPLPEDIRQDLQDFHQDLLAHCGIQLEGEEEEPEEETSLSSRLRSLLETVRLVKKKEEKPEEELPAEEKKPQSLQELVSHMVVRWAQEDYVQSPELVRAMFSLLHRQYDGLGELLRALPRAYTISPSSVEDTMSLLECLGQIRSLLIVQMGPQEENLMIQSIGNIMNNKVFYQHPNLMRALGMHETVMEVMVNVLGGGETKEIRFPKMVTSCCRFLCYFCRISRQNQRSMFDHLSYLLENSGIGLGMQGSTPLDVAAASVIDNNELALALQEQDLEKVVSYLAGCGLQSCPMLLAKGYPDIGWNPCGGERYLDFLRFAVFVNGESVEENANVVVRLLIRKPECFGPALRGEGGSGLLAAIEEAIRISEDPARDGPGVRRDRRREHFGEEPPEENRVHLGHAIMSFYAALIDLLGRCAPEMHLIQAGKGEALRIRAILRSLVPLDDLVGIISLPLQIPTLGKDGALVQPKMSASFVPDHKASMVLFLDRVYGIENQDFLLHVLDVGFLPDMRAAASLDTATFSTTEMALALNRYLCLAVLPLITKCAPLFAGTEHRAIMVDSMLHTVYRLSRGRSLTKAQRDVIEDCLMALCRYIRPSMLQHLLRRLVFDVPILNEFAKMPLKLLTNHYERCWKYYCLPTGWANFGVTSEEELHLTRKLFWGIFDSLAHKKYDQELYRMAMPCLCAIAGALPPDYVDASYSSKAEKKATVDAEGNFDPRPVETLNVIIPEKLDSFINKFAEYTHEKWAFDKIQNNWSYGENVDEELKTHPMLRPYKTFSEKDKEIYRWPIKESLKAMIAWEWTIEKAREGEEERTEKKKTRKISQTAQTYDPREGYNPQPPDLSGVTLSRELQAMAEQLAENYHNTWGRKKKQELEAKGGGTHPLLVPYDTLTAKEKARDREKAQELLKFLQMNGYAVTRGLKDMELDTSSIEKRFAFGFLQQLLRWMDISQEFIAHLEAVVSSGRVEKSPHEQEIKFFAKILLPLINQYFTNHCLYFLSTPAKVLGSGGHASNKEKEMITSLFCKLAALVRHRVSLFGTDAPAVVNCLHILARSLDARTVMKSGPEIVKAGLRSFFESASEDIEKMVENLRLGKVSQARTQVKGVGQNLTYTTVALLPVLTTLFQHIAQHQFGDDVILDDVQVSCYRTLCSIYSLGTTKNTYVEKLRPALGECLARLAAAMPVAFLEPQLNEYNACSVYTTKSPRERAILGLPNSVEEMCPDIPVLDRLMADIGGLAESGARYTEMPHVIEITLPMLCSYLPRWWERGPEAPPPALPAGAPPPCTAVTSDHLNSLLGNILRIIVNNLGIDEATWMKRLAVFAQPIVSRARPELLHSHFIPTIGRLRKRAGKVVAEEEQLRLEAKAEAEEGELLVRDEFSVLCRDLYALYPLLIRYVDNNRAHWLTEPNANAEELFRMVGEIFIYWSKSHNFKREEQNFVVQNEINNMSFLTADSKSKMAKAGDAQSGGSDQERTKKKRRGDRYSVQTSLIVATLKKMLPIGLNMCAPTDQDLIMLAKTRYALKDTDEEVREFLQNNLHLQGKVEGSPSLRWQMALYRGLPGREEDADDPEKIVRRVQEVSAVLYHLEQTEHPYKSKKAVWHKLLSKQRRRAVVACFRMTPLYNLPTHRACNMFLESYKAAWILTEDHSFEDRMIDDLSKAGEQEEEEEEVEEKKPDPLHQLVLHFSRTALTEKSKLDEDYLYMAYADIMAKSCHLEEGGENGEAEEEEVEVSFEEKEMEKQRLLYQQSRLHTRGAAEMVLQMISACKGETGAMVSSTLKLGISILNGGNAEVQQKMLDYLKDKKEVGFFQSIQALMQTCSVLDLNAFERQNKAEGLGMVNEDGTVINRQNGEKVMADDEFTQDLFRFLQLLCEGHNNDFQNYLRTQTGNTTTINIIICTVDYLLRLQESISDFYWYYSGKDVIEEQGKRNFSKAMSVAKQVFNSLTEYIQGPCTGNQQSLAHSRLWDAVVGFLHVFAHMMMKLAQDSSQIELLKELLDLQKDMVVMLLSLLEGNVVNGMIARQMVDMLVESSSNVEMILKFFDMFLKLKDIVGSEAFQDYVTDPRGLISKKDFQKAMDSQKQFTGPEIQFLLSCSEADENEMINFEEFANRFQEPARDIGFNVAVLLTNLSEHVPHDPRLRNFLELAESILEYFRPYLGRIEIMGASRRIERIYFEISETNRAQWEMPQVKESKRQFIFDVVNEGGEAEKMELFVSFCEDTIFEMQIAAQISEPEGEPEADEDEGMGEAAAEGAEEGAAGAEGAAGTVAAGATARLAAAAARALRGLSYRSLRRRVRRLRRLTAREAATALAALLWAVVARAGAAGAGAAAGALRLLWGSLFGGGLVEGAKKVTVTELLAGMPDPTSDEVHGEQPAGPGGDADGAGEGEGEGDAAEGDGDEEVAGHEAGPGGAEGVVAVADGGPFRPEGAGGLGDMGDTTPAEPPTPEGSPILKRKLGVDGEEEELVPEPEPEPEPEPEKADEENGEKEEVPEAPPEPPKKAPPSPPAKKEEAGGAGMEFWGELEVQRVKFLNYLSRNFYTLRFLALFLAFAINFILLFYKVSDSPPGEDDMEGSAAGDLAGAGSGGGSGWGSGAGEEAEGDEDENMVYYFLEESTGYMEPALWCLSLLHTLVAFLCIIGYNCLKVPLVIFKREKELARKLEFDGLYITEQPGDDDVKGQWDRLVLNTPSFPSNYWDKFVKRKVLDKHGDIFGRERIAELLGMDLASLEITAHNERKPDPPPGLLTWLMSIDVKYQIWKFGVIFTDNSFLYLGWYMVMSLLGHYNNFFFAAHLLDIAMGVKTLRTILSSVTHNGKQLVMTVGLLAVVVYLYTVVAFNFFRKFYNKSEDEDEPDMKCDDMMTCYLFHMYVGVRAGGGIGDEIEDPAGDEYELYRVVFDITFFFFVIVILLAIIQGLIIDAFGELRDQQEQVKEDMETKCFICGIGSDYFDTTPHGFETHTLEEHNLANYMFFLMYLINKDETEHTGQESYVWKMYQERCWDFFPAGDCFRKQYEDQLS'
            ]

short_test_sequences = ['MEKLEVGIYTRAREGEIACGDACLVKRVEGVIFLAVGDGIGHGPEAARAAEIAIASMESSMNTGLVNIFQLCHRELRGTRGAVAALCRVDRRQGLWQAAIVGNIHVKILSAKGIITPLATPGILGYNYPHQLLIAKGSYQEGDLFLIHSDGIQEGAVPLALLANYRLTAEELVRLIGEKYGRRDDDVAVIVAR',
                        'PNFSGNWKIIRSENFEELLKVLGVNVMLRKIAVAAASKPAVEIKQEGDTFYIKTSTTVRTTEINFKVGEEFEEQTVDGRPCKSLVKWESENKMVCEQKLLKGEGPKTSWTRELTNDGELILTMTADDVVCTRVYVRE',
                        'PSVYDAAAQLTADVKKDLRDSWKVIGSDKKGNGVALMTTLFADNQETIGYFKRLGDVSQGMANDKLRGHSIILMYALQNFIDQLDNPDDLVCVVEKFAVNHITRKISAAEFGKINGPIKKVLASKNFGDKYANAWAKLVAVVQAAL',
                        'PSVYDAAAQLTADVKKDLRDSWKVIGSDKKGNGVALMTTLFADNQETIGYFKRLGDVSQGMANDKLRGHSIILMYALXXXDQLDNPDDLVCVVEKFAVNHITRKISAAEFGKINGPIKKVLASKNFGDKYANAWAKLVAVVQAAL']

class TestSeqAlign(unittest.TestCase):


    def test_align_complete(self):
        for sequence in short_test_sequences:
            sa = SequenceAlign(sequence1=sequence, sequence2=sequence)
            aligned, error = sa.do_sequence_alignment()
            self.assertTrue(aligned)

    def test_align_subset(self):
        for sequence in short_test_sequences:
            for seq_range in (slice(20), slice(50), slice(100), slice(150), slice(200), slice(250)):
                sa = SequenceAlign(sequence1=sequence, sequence2=sequence[seq_range])
                aligned, error = sa.do_sequence_alignment()
                self.assertTrue(aligned)

    def test_align_misalign(self):
        for sequence in short_test_sequences:
            for seq_range in (slice(10), slice(20), slice(50), slice(100), slice(150), slice(200), slice(250)):
                sa = SequenceAlign(sequence1=sequence[seq_range], sequence2=no_match)
                aligned, error = sa.do_sequence_alignment()
                self.assertFalse(aligned)
        
    def test_align_changing_length_to_2000(self):
        for seq_range in (slice(500), slice(1000), slice(1500), slice(2000), slice(2000)):
            sa = SequenceAlign(sequence1=test_sequences[2][seq_range], sequence2=test_sequences[2][20:200])
            aligned, error = sa.do_sequence_alignment()
            self.assertTrue(aligned)

    def test_align_changing_length_over_2500(self):
        for seq_range in (slice(2500), slice(3000), slice(3500), slice(4000), slice(4500)):
            sa = SequenceAlign(sequence1=test_sequences[2][seq_range], sequence2=test_sequences[2][20:200])
            aligned, error = sa.do_sequence_alignment()
            self.assertTrue(aligned)


    def test_align_pairwise2_changing_length_to_2000(self):
        for seq_range in (slice(500), slice(1000), slice(1500), slice(2000), slice(2000)):
            sa = SequenceAlign(sequence1=test_sequences[2][seq_range], sequence2=test_sequences[2][20:200])
            sa.pairwise2()
            s = sa.do_sequences_align()
            self.assertTrue(s)

    def test_align_pairwise2_changing_length_over_2500(self):
        for seq_range in (slice(2500), slice(3000), slice(3500), slice(4000), slice(4500)):
            sa = SequenceAlign(sequence1=test_sequences[2][seq_range], sequence2=test_sequences[2][20:200])
            sa.pairwise2()
            s = sa.do_sequences_align()
            self.assertFalse(s)

    def test_align_pairwise2_changing_slice(self):
        for seq_range in (slice(20), slice(50), slice(100), slice(150), slice(200), slice(250)):
            sa = SequenceAlign(sequence1=short_test_sequences[0], sequence2=short_test_sequences[0][seq_range])
            sa.pairwise2()
            s = sa.do_sequences_align()
            self.assertTrue(s)
    
    def test_align_pairwise2_misalign(self):
        for sequence in short_test_sequences:
            sa = SequenceAlign(sequence1=sequence, sequence2=no_match)
            sa.pairwise2()
            s = sa.do_sequences_align()
            self.assertFalse(s)

    def test_align_pairwise_aligner_changing_length_to_5000(self):
        for seq_range in (slice(500), slice(1000), slice(1500), slice(2000), slice(2000), slice(2500), slice(3000), slice(3500), slice(4000), slice(4500), slice(5000)):
            sa = SequenceAlign(sequence1=test_sequences[2][seq_range], sequence2=test_sequences[2][20:200])
            sa.pairwise_aligner()
            s = sa.do_sequences_align()
            self.assertTrue(s)

    def test_align_pairwise_aligner_nucleotide_changing_length_to_5000(self):
        for seq_range in (slice(500), slice(1000), slice(1500), slice(2000), slice(2000), slice(2500), slice(3000), slice(3500), slice(4000), slice(4500), slice(5000)):
            sa = SequenceAlign(sequence1=test_sequences[1][seq_range], sequence2=test_sequences[1][20:200])
            sa.pairwise_aligner()
            s = sa.do_sequences_align()
            self.assertTrue(s)

    def test_align_pairwise_aligner_changing_slice(self):
        for seq_range in (slice(20), slice(50), slice(100), slice(150), slice(200), slice(250)):
            sa = SequenceAlign(sequence1=short_test_sequences[0], sequence2=short_test_sequences[0][seq_range])
            sa.pairwise_aligner()
            s = sa.do_sequences_align()
            self.assertTrue(s)
    
    def test_align_pairwise_aligner_misalign(self):
        for sequence in test_sequences:
            sa = SequenceAlign(sequence1=sequence, sequence2=no_match)
            sa.pairwise_aligner()
            s = sa.do_sequences_align()
            self.assertFalse(s)



if __name__ == '__main__':
    unittest.main()