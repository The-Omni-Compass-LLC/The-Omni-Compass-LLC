(()=>{ /* 🌍 THE TEN MOST WIDELY KNOWN RELIGIONS (v248), first on the Cultures & Religion page: where each began, its sacred writings and
   its central teaching, in neutral words, with a link out to a full reference article for anyone who wants more. The order begins with
   the largest by followers worldwide; counts for the smaller traditions vary by source, so no rank is claimed below the first four. */
 const $=id=>document.getElementById(id); const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const R=[['✝️','Christianity','Began in the 1st century CE in Judea, from the life and teaching of Jesus of Nazareth.','The Bible (Old and New Testaments).','One God; Jesus as the Christ, whose death and resurrection offer salvation; love of God and neighbour.','https://www.britannica.com/topic/Christianity'],
  ['☪️','Islam','Began in the 7th century CE in Arabia, through the Prophet Muhammad.','The Qur’an, with the Hadith (sayings and deeds of the Prophet).','One God (Allah); Muhammad as the final prophet; the Five Pillars of faith, prayer, charity, fasting and pilgrimage.','https://www.britannica.com/topic/Islam'],
  ['🕉️','Hinduism','Grew over thousands of years in South Asia, with no single founder.','The Vedas, the Upanishads, the Bhagavad Gita and the epics.','Dharma (right living), karma, rebirth, and liberation (moksha); many forms of the divine.','https://www.britannica.com/topic/Hinduism'],
  ['☸️','Buddhism','Began about the 5th century BCE in India, from the teaching of Siddhartha Gautama, the Buddha.','The Pali Canon (Tipitaka) and the Mahayana sutras.','The Four Noble Truths and the Eightfold Path lead beyond suffering to nirvana.','https://www.britannica.com/topic/Buddhism'],
  ['☯️','Chinese traditional religion and Taoism','Grew in China over thousands of years, joining folk practice, ancestor veneration, Taoism and Confucian ethics.','The Tao Te Ching and the Zhuangzi (Taoism); the Analects (Confucianism).','Harmony with the Tao (the Way), honour of ancestors, balance of yin and yang.','https://www.britannica.com/topic/Chinese-religion'],
  ['🪯','Sikhism','Began in the 15th century CE in the Punjab, from Guru Nanak and the nine Gurus after him.','The Guru Granth Sahib.','One God; honest work, sharing with others and remembering God; equality of all people.','https://www.britannica.com/topic/Sikhism'],
  ['✡️','Judaism','Began over 3,000 years ago with the covenant of the people of Israel.','The Hebrew Bible (Tanakh), above all the Torah, and the Talmud.','One God; the covenant and the commandments; justice, study and the life of the community.','https://www.britannica.com/topic/Judaism'],
  ['🌟','Bahá’í Faith','Began in the 19th century CE in Persia, from the Báb and Bahá’u’lláh.','The writings of Bahá’u’lláh, among them the Kitáb-i-Aqdas.','One God, the unity of religions and the oneness of humanity.','https://www.britannica.com/topic/Bahai-Faith'],
  ['🤲','Jainism','Taught in India by Mahavira in the 6th to 5th centuries BCE, the last of 24 Tirthankaras.','The Agamas.','Ahimsa (non-violence toward every living being), truthfulness and non-attachment.','https://www.britannica.com/topic/Jainism'],
  ['⛩️','Shinto','The native tradition of Japan, from ancient times, with no single founder.','The Kojiki and the Nihon Shoki (early chronicles).','The kami (sacred spirits) in nature, ancestors and places; purity, ritual and the shrine.','https://www.britannica.com/topic/Shinto']];
 const css=document.createElement('style'); css.textContent=`
#kFaith10{margin:10px 0 16px;padding:12px;border-radius:4px 18px 4px 18px;background:linear-gradient(160deg,rgba(60,40,10,.55),rgba(20,12,4,.6));border:1px solid rgba(255,214,120,.45)}
#kFaith10 h3{margin:0 0 4px;font:900 20px system-ui,sans-serif;color:#ffd678}
#kFaith10 .f10Grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px;margin-top:8px}
#kFaith10 .f10{background:rgba(0,0,0,.28);border-left:3px solid #ffd678;border-radius:2px 12px 2px 12px;padding:10px}
#kFaith10 .f10 b{font:900 16px system-ui,sans-serif}
#kFaith10 .f10 p{margin:4px 0;font-size:13.5px;line-height:1.45}
#kFaith10 .f10 a{display:inline-block;margin-top:4px;color:#ffd678;font-weight:800}
#kFaith10 small{opacity:.8}`; document.head.appendChild(css);
 function mount(){ const d=$('kRelig'); if(!d||d.hidden) return; const inn=d.querySelector('.rgIn'); if(!inn||inn.querySelector('#kFaith10')) return;
  const box=document.createElement('section'); box.id='kFaith10';
  box.innerHTML='<h3>🌍 The 10 most widely known religions</h3><small>Where each began, its sacred writings and its central teaching, in neutral words. The first four are the largest by followers worldwide; counts for the others vary by source. Each card links out to a full reference article.</small><div class="f10Grid">'+R.map((r,i)=>'<div class="f10"><b>'+(i+1)+'. '+r[0]+' '+esc(r[1])+'</b><p><b>Began:</b> '+esc(r[2])+'</p><p><b>Writings:</b> '+esc(r[3])+'</p><p><b>Teaching:</b> '+esc(r[4])+'</p><a href="'+r[5]+'" target="_blank" rel="noopener">Read more ↗</a></div>').join('')+'</div><p><a href="https://www.pewresearch.org/religion/" target="_blank" rel="noopener" style="color:#ffd678;font-weight:800">Pew Research Center: the world’s religions in numbers ↗</a></p>';
  const h=inn.querySelector('h2'); if(h&&h.nextSibling) inn.insertBefore(box,h.nextSibling.nextSibling||null); else inn.insertBefore(box,inn.firstChild); }
 setInterval(mount,700);
 window.KFAITH10={list:()=>R.map(r=>r[1])};
})();
