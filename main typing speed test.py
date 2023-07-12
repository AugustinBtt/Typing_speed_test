import random
import tkinter as tk
from tkinter import messagebox

words_bank = ['ashamed', 'dog', 'wall', 'spotless', 'cub', 'numerous', 'hour', 'waste', 'loutish', 'torpid', 'fuel', 'carriage', 'poor', 'flash', 'minute', 'love', 'size', 'stain', 'disturbed', 'creepy', 'acrid', 'squealing', 'muddled', 'rampant', 'shape', 'whine', 'unique', 'voiceless', 'bore', 'ruthless', 'cuddly', 'neighborly', 'bedroom', 'loaf', 'disastrous', 'kneel', 'famous', 'abnormal', 'space', 'excuse', 'dirty', 'sharp', 'gaudy', 'amuck', 'improve', 'bumpy', 'scared', 'high-pitched', 'horse', 'frightened', 'mellow', 'kind', 'entertaining', 'ignore', 'delightful', 'desert', 'absurd', 'ear', 'wind', 'lopsided', 'earsplitting', 'beam', 'mountain', 'simplistic', 'spiffy', 'correct', 'pack', 'graceful', 'nutty', 'analyze', 'boot', 'synonymous', 'separate', 'wild', 'voracious', 'lyrical', 'wax', 'inexpensive', 'encouraging', 'heal', 'suit', 'egg', 'towering', 'skinny', 'normal', 'horses', 'wave', 'didactic', 'historical', 'breakable', 'rainstorm', 'trousers', 'gratis', 'spicy', 'need', 'tomatoes', 'calculating', 'direction', 'second', 'preserve', 'guide', 'adaptable', 'sound', 'attractive', 'zoom', 'winter', 'hulking', 'trashy', 'skirt', 'risk', 'parallel', 'store', 'reach', 'endurable', 'rapid', 'maddening', 'pickle', 'stew', 'jar', 'idiotic', 'bear', 'judge', 'example', 'public', 'ripe', 'picayune', 'downtown', 'rhyme', 'necessary', 'honey', 'flame', 'rebel', 'trust', 'hall', 'overrated', 'handy', 'trucks', 'skillful', 'crooked', 'advertisement', 'unknown', 'press', 'slope', 'soothe', 'abounding', 'stop', 'puncture', 'important', 'juvenile', 'dirt', 'racial', 'airplane', 'childlike', 'knowing', 'handle', 'learned', 'statuesque', 'jellyfish', 'blade', 'fantastic', 'hunt', 'shock', 'bounce', 'hobbies', 'clever', 'expert', 'untidy', 'six', 'long', 'sofa', 'super', 'concern', 'hesitant', 'behavior', 'exclusive', 'achiever', 'sour', 'boast', 'ancient', 'scrawny', 'cable', 'verdant', 'potato', 'abaft', 'tramp', 'vulgar', 'listen', 'office', 'title', 'deer', 'daffy', 'slippery', 'happy', 'label', 'brother', 'sulky', 'feeling', 'ban', 'decay', 'cave', 'unused', 'perfect', 'cannon', 'shiver', 'dear', 'difficult', 'orange', 'neat', 'innate', 'obtain', 'calendar', 'shop', 'automatic', 'dust', 'adhesive', 'note', 'receive', 'sparkling', 'imperfect', 'null', 'mixed', 'glamorous', 'dime', 'hook', 'married', 'unbecoming', 'pet', 'check', 'trains', 'flock', 'equable', 'scratch', 'tense', 'admit', 'sniff', 'fabulous', 'mate', 'crazy', 'fax', 'suspend', 'ball', 'guarded', 'bite', 'shade', 'church', 'strip', 'history', 'gifted', 'force', 'slip', 'miniature', 'mindless', 'imagine', 'courageous', 'crabby', 'drab', 'curvy', 'mice', 'attempt', 'pathetic', 'guarantee', 'faded', 'rule', 'cheat', 'spurious', 'paddle', 'beg', 'yell', 'slap', 'steady', 'quixotic', 'rescue', 'ruddy', 'picture', 'calculate', 'neck', 'harsh', 'sleet', 'finicky', 'blow', 'spy', 'box', 'drown', 'list', 'thought', 'ill', 'closed', 'general', 'lame', 'condition', 'uneven', 'baseball', 'venomous', 'run', 'unruly', 'dream', 'reflect', 'unable', 'clam', 'hurried', 'cup', 'grieving', 'inject', 'bloody', 'depressed', 'stomach', 'week', 'advise', 'pie', 'brawny', 'plantation', 'brown', 'crib', 'medical', 'smell', 'sore', 'fire', 'cooing', 'sail', 'divergent', 'scandalous', 'prepare', 'straight', 'arrive', 'edge', 'pushy', 'mitten', 'frequent', 'ahead', 'attend', 'ignorant', 'diligent', 'rabid', 'male', 'whisper', 'dependent', 'claim', 'drum', 'complex', 'wait', 'parched', 'volleyball', 'combative', 'brave', 'club', 'humdrum', 'squash', 'naughty', 'damaging', 'talk', 'cook', 'wonder', 'moon', 'serious', 'front', 'trail', 'imaginary', 'stranger', 'scrub', 'cover', 'aloof', 'tiresome', 'vest', 'cemetery', 'happen', 'cut', 'examine', 'dusty', 'bad', 'notebook', 'deeply', 'finger', 'hat', 'oafish', 'snow', 'level', 'hang', 'alcoholic', 'shrill', 'volatile', 'bang', 'ground', 'pine', 'bell', 'scarce', 'hollow', 'plausible', 'aggressive', 'pear', 'selfish', 'surprise', 'crack', 'witty', 'cent', 'robust', 'shaky', 'work', 'selection', 'symptomatic', 'giant', 'treat', 'fuzzy', 'basketball', 'bouncy', 'pets', 'rigid', 'cake', 'languid', 'describe', 'spell', 'rare', 'lamentable', 'tempt', 'distinct', 'wealth', 'rob', 'value', 'frame', 'decision', 'fluffy', 'lumber', 'floor', 'present', 'summer', 'nail', 'steer', 'country', 'dislike', 'stay', 'whimsical', 'plant', 'bubble', 'well-groomed', 'save', 'stupendous', 'nippy', 'homely', 'snail', 'joke', 'rabbits', 'pan', 'distance', 'fresh', 'flippant', 'payment', 'try', 'signal', 'ceaseless', 'short', 'pass', 'murder', 'substantial', 'innocent', 'scarf', 'needle', 'government', 'disappear', 'acidic', 'crowded', 'cough', 'gaze', 'profuse', 'treatment', 'joyous', 'complete', 'wheel', 'obsolete', 'keen', 'cloudy', 'brass', 'lean', 'moldy', 'gorgeous', 'soda', 'irritating', 'unaccountable', 'guitar', 'guttural', 'flimsy', 'adventurous', 'crawl', 'instruct', 'berry', 'heap', 'leg', 'weary', 'night', 'dizzy', 'question', 'shallow', 'smash', 'actor', 'bag', 'resonant', 'milky', 'ghost', 'route', 'educate', 'fruit', 'rely']

window = tk.Tk()
window.geometry("910x500")
window.title("Typing speed test")

countdown_id = None

def test_on():
    global countdown_id

    test_words = random.sample(words_bank, k=100)

    text = tk.Text(window)


    time_label = tk.Label(window, text=" ", font= 4)
    time_label.grid(row=0, column=0)


    cpm = tk.Label(window, text="0", font= 4)
    cpm.grid(row=0, column=0, sticky= 'W')

    wpm = tk.Label(window, text= 0, font= 4)
    wpm.grid(row=0, column=0, sticky= 'E')


    text.insert('insert', '   '.join(test_words))
    text.config(font=3, height= 10, width= 80)
    text.grid(row=1, column=0, padx=10, sticky='nsew')

    entry_label = tk.Label(window, text='User input:', font= 5, pady= 40)
    entry_label.grid(row=2, column=0)

    user_entry = tk.Entry(window,width=100)
    user_entry.grid(row=3, column=0)


    def countdown(time):
        global countdown_id
        if time > 0:
            time_label['text'] = time
            countdown_id = window.after(1000, countdown, time-1)
            character_count()
            words_count()
        else:
            time_label.config(fg='orange')
            time_label['text'] = "Time is up!"
            entry_label.config(state="disabled")
            user_entry.config(state="disabled")
            messagebox.showinfo("Your results", f"Characters per minute: {cpm['text']}" f"\nWords per minute: {wpm['text']}")


    def character_count():
        count = user_entry.get()
        count_no_spaces = count.replace(' ', '')
        cpm['text'] = len(count_no_spaces)

    counted_words = set()

    def words_count():
        full_string = user_entry.get().split()
        user_words = set(full_string)
        current_count = int(wpm['text'])

        for word in test_words:
            if word in user_words and word not in counted_words:
                current_count += 1
                counted_words.add(word)

                start_index = '1.0'
                while True:
                    start_index = text.search(word, start_index, 'end')
                    if not start_index:
                        break
                    end_index = f'{start_index}+{len(word)}c'
                    text.tag_add(word,start_index, end_index)
                    text.tag_config(word, background='orange')

                    start_index = end_index

        wpm['text'] = str(current_count)


    def reset():
        global countdown_id
        if countdown_id:
            window.after_cancel(countdown_id)
            countdown_id = None
        test_on()
        cpm.config(text="0")
        wpm.config(text="0")
        time_label['text'] = ' '

    empty_row = tk.Frame(window, height=40)
    empty_row.grid(row=4, column=0)

    restart_button = tk.Button(text='Restart', command=reset, pady=10, padx=10)
    restart_button.grid(row=5, column=0)

    countdown(60)

test_on()

window.mainloop()