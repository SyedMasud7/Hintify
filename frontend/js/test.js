// Test management
class TestManager {
    constructor() {
        this.questions = [];
        this.currentQuestionIndex = 0;
        this.currentQuestion = null;
        this.timeStarted = null;
        this.hintUsed = false;
        this.score = 0;
        this.subjectId = null;
    }

    startQuestions(questions, subjectId) {
        this.questions = questions;
        this.currentQuestionIndex = 0;
        this.score = 0;
        this.subjectId = subjectId;
        this.timeStarted = Date.now();
        this.loadCurrentQuestion();
        this.showTestModal();
    }

    loadCurrentQuestion() {
        if (this.currentQuestionIndex < this.questions.length) {
            this.currentQuestion = this.questions[this.currentQuestionIndex];
            this.renderQuestion();
        } else {
            this.finishTest();
        }
    }

    renderQuestion() {
        const content = document.getElementById('testContent');
        const progress = ((this.currentQuestionIndex + 1) / this.questions.length) * 100;

        content.innerHTML = `
            <div class="test-progress">
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${progress}%"></div>
                </div>
                <div class="progress-text">
                    Question ${this.currentQuestionIndex + 1} of ${this.questions.length}
                </div>
            </div>

            <div class="question-container">
                <div class="question-header">
                    <span class="difficulty-badge difficulty-${this.currentQuestion.difficulty}">
                        ${this.currentQuestion.difficulty.toUpperCase()}
                    </span>
                </div>

                <div class="question-text">
                    <h4>${this.currentQuestion.question_text}</h4>
                </div>

                <div class="choices-container">
                    ${this.currentQuestion.choices.map(choice => `
                        <div class="choice-option" onclick="selectChoice(${choice.id})" data-choice-id="${choice.id}">
                            <div class="choice-letter">${choice.letter}</div>
                            <div class="choice-text">${choice.choice_text}</div>
                        </div>
                    `).join('')}
                </div>

                <div class="question-actions">
                    <button class="btn btn-outline" onclick="getHint()" ${this.hintUsed ? 'disabled' : ''}>
                        <i class="fas fa-lightbulb"></i>
                        ${this.hintUsed ? 'Hint Used' : 'Get Hint'}
                    </button>
                    <button class="btn btn-primary" onclick="submitAnswer()" disabled id="submitBtn">
                        <i class="fasck"></i>
                        Submiwer
                    </
/div>

                <div class="hint-container hid">
                    <div class="hint-content">
                        <i class="fas fa-lightbulb"></i>
                        <sn>
                    </>
                </div>
          v>


        // Update modal title
        document.getElementByITest`;
     
    }

    getSubjectName() {
        if (subjectsManager && subjectsManager.) {
     ;
st';
        }
        return 'Test';
 }

    async getHint() {


        try {
            const response = await fetch(`/api/questions/${this.currentQuestion.id}/hint`);

            if (response.ok) {
             e.json();
                this.show');
            } else {
                this.showHint('Think about the key concepts in this question;
          }
        ) {
            console.error('Er
        
        }
        
        this.hintUsed = true;
        
     
');
        if (hintBtn) {
            hintBtn.disabled = true;
            hintBtn.innerHTML = '<i class="fas fa-lightbulb"></i> Hi
        }
    }

    s
ainer');
        const hintTextElemText');
        
        if (hintContainer && hintTex
;
            hintContainer.classList.remove('hidden');
        
    }

    submitAnswer() {
        
        if (!selectedChourn;

        coiceId);
       
        // Check if answer is c
        // Since we don't expose cI
        this.checkAnswer(choiceId);
    }

    aeId) {
{
            const response = a
                method: 'POST'
            });

            if (response.ok) {
                const result = await re;
                
                if (result.is_correct) {
                    thre++;
                }

                sult({
                    is_correct: result.is_correct,
                    correct_choice_id: result.correct_choice_id,
                    explanation: result.explanation || `This is question ${this.currentQuestionIndex + 1} fro`
                });
 {
                throw new Error('Failed to c
            }
        } catch (error) {
            console.error('Error checking answer:', error);
            // Fallback: assuemo
            this.score++;
            this.s({
           true,
     d,

            });
        }
    }

sult) {
        const content ');
        const isCorrect = result.is_correct;
       

            <div cla>
                <div class="result-ict'}">
                    <i class=">
                /div>
                
                <h3>${isCorrect ? 'Correct/h3>
                
         
     >

                </v>

                <div class="result-actions">
        ">
                        $tion'}
                        <i class="fas ${/i>
                    </button>
                </div>
            </div>
        `;
    }

    g) {

        return choice ? `${cho'';
    }

    isLastQuestion() {
        return this.currentQuestionInd;
    }

    nextQuestion() {
        if (this.isLas) {

        } else {
            this.currentQuestionIndex++;
            this.timeStarted = Date.now();
            this.loadCurrentQuestion();
        }
    }

    finishTest() {
        const totalTime = 
        const accuracy = (this.score / this * 100;
        
        const summary = {
            correct_answer
            total_ques
y,
            time_taken: totalTime
        };
        
        this.showTestSummary(;
    }

    showTestSummary(summary) {
        const content ');
        
        co`
     
>
                    <i cl></i>
                    <h3>Test Complete!</h3>
                </div>

     >
t-card">
                     s}</div>
                        <div class="stat-label">Correct Answers</div>
                    </div>
     >

                        
                    </div>
                    <div clasard">
                        <div class="s
                        <div class="stat-label">Time Taken<v>
                    </div>
                </div>

                <div clas">
                    <butt
                  >
          her Test
     
 )">
>
                   
                    </button>
                </div>
            </div>
        `;
    }

    formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes}:${remainingSeconds.t}`;
    }

    showTestModal() {
 );
l) {
            modal.clden');
            document.body.';
 
 }

    showError(message) {
 ontent');
L = `
            <div class="err">
                <i class="fas fa-exclamation-triangle"></i>
                <h3>Error</h3>
                <p>${message}</p>
                <button class="btn btn-pr">
 

            </div>
        `;// Global functionstion seleager();
});Manw Test = nenager
    testMa () => {Loaded',MContentner('DOListedEventment.adcu;
donagert testMager
let manaze tesialinit
}

// I 0;
    }ionIndex =rrentQuestr.cutManage
        tess = [];ger.questionana testM   {
    tManager) tes  if (    
    }
;
   = 'auto'le.overflowy.sty.boddocument   en');
     t.add('hidddal.classLis
        mo (modal) { if;
   testModal')entById('getElemcument.donst modal =     codal() {
 closeTestMo
function

}    }tAnswer();
.submiManager        test{
estManager) if (t{
    Answer() ubmitction s
}

fun();
    }tHintager.ge testMan      ger) {
 f (testMana) {
    ietHint( gunction  }
}

f }
  se;
       d = falblesan.disubmitBt         Btn) {
     if (submit   n');
   tBtmiyId('sublementBt.getEocumen dtBtn =t submiconsn
        buttobmit  sublena       // E
  
       ected');seldd('assList.aclectedOption.sel  
       {ectedOption)el   if (s"]`);
 }ceId"${choie-id=hoicta-cector(`[dant.querySelocumetion = delectedOp s   constchoice
 rent / Select cur  /);
    
  
    }elected');st.remove('sclassLiion.       opttion => {
 h(op.forEacn')ice-optio('.choelectorAllent.queryS   docum
 ectionrevious selve pemo {
    // RhoiceId)(ccectChoi
func


    }
}