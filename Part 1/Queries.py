import os
import pandas as pd
from collections import defaultdict

# Διαδρομή του φακέλου με τα κείμενα
docs_folder = 'D:/ΣΧΟΛΗ/Ανάκτηση Πληροφορίας/Project/Queries/Queries'

# Δημιουργία λεξικού για την καταμέτρηση των λέξεων
word_counts = defaultdict(lambda: defaultdict(int))

# Επεξεργασία αρχείων
for filename in os.listdir(docs_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(docs_folder, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            
            # Καταμέτρηση των λέξεων
            for word in words:
                word_counts[word][filename] += 1

# Δημιουργία DataFrame
df = pd.DataFrame(word_counts).fillna(0)
df.index.name = 'Word'

# Αποθήκευση σε αρχείο CSV
df.to_csv('D:/ΣΧΟΛΗ/Ανάκτηση Πληροφορίας/Project/word_querie_freq_.csv', encoding='utf-8')

# Διάβασμα του αρχείου CSV που δημιουργήσατε προηγουμένως
df = pd.read_csv('D:/ΣΧΟΛΗ/Ανάκτηση Πληροφορίας/Project/word_querie_freq_.csv', index_col='Word')

# Αναστροφή του DataFrame
df_transposed = df.transpose()

# Αποθήκευση του αναστραμμένου DataFrame σε ένα νέο αρχείο CSV
df_transposed.to_csv('D:/ΣΧΟΛΗ/Ανάκτηση Πληροφορίας/Project/word_querie_freq_transposed.csv', encoding='utf-8')
