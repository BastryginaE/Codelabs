using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Media;

namespace LanguageTutor
{
    public partial class Form1 : Form
    {
        public static int p;
        public Form1()
        {
            InitializeComponent();
        }

      

       
       

       

        private void button1_Click(object sender, EventArgs e)
        {
            Button button = sender as Button;
            switch (button.Name)
            {
                case "button1":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"A.wav");
                        Sd.Play(); p = 1; break;
                    }
                case "button2":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"B.wav");
                        Sd.Play(); p = 2; break;
                    }
               
                case "button4":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"C.wav");
                        Sd.Play(); p = 4; break;
                    }
                case "button5":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"D.wav");
                        Sd.Play(); p = 5; break;
                    }
                case "button6":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"E.wav");
                        Sd.Play(); p = 6; break;
                    }
                case "button7":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"F.wav");
                        Sd.Play(); p = 7; break;
                    }
                case "button8":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"G.wav");
                        Sd.Play(); p = 8; break;
                    }
                case "button9":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"H.wav");
                        Sd.Play(); p = 9; break;
                    }
                case "button10":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"I.wav");
                        Sd.Play(); p = 10; break;
                    }
                case "button11":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"J.wav");
                        Sd.Play(); p = 11; break;
                    }
                case "button12":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"K.wav");
                        Sd.Play(); p = 12; break;
                    }
                case "button13":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"L.wav");
                        Sd.Play(); p = 13; break;
                    }
                case "button14":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"M.wav");
                        Sd.Play(); p = 14; break;
                    }
                case "button15":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"N.wav");
                        Sd.Play(); p = 15; break;
                    }
                case "button16":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"O.wav");
                        Sd.Play(); p = 16; break;
                    }
                case "button17":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"P.wav");
                        Sd.Play(); p = 17; break;
                    }
                case "button18":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"Q.wav");
                        Sd.Play(); p = 18; break;
                    }
                case "button19":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"R.wav");
                        Sd.Play(); p = 19; break;
                    }
                case "button20":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"S.wav");
                        Sd.Play(); p = 20; break;
                    }
                case "button21":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"T.wav");
                        Sd.Play(); p = 21; break;
                    }
                case "button22":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"U.wav");
                        Sd.Play(); p = 22; break;
                    }
                case "button23":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"V.wav");
                        Sd.Play(); p = 23; break;
                    }
                case "button24":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"W.wav");
                        Sd.Play(); p = 24; break;
                    }
               case "button25":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"X.wav");
                        Sd.Play(); p = 25; break;
                    }
                case "button26":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"Y.wav");
                        Sd.Play(); p = 26; break;
                    }
               case "button27":
                    {
                        SoundPlayer Sd = new SoundPlayer(@"Z.wav");
                        Sd.Play(); p = 27; break;

                    }

            }
            Form1.ActiveForm.Hide();
            Form2 secondForm = new Form2();
            secondForm.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form1.ActiveForm.Hide();
            Form3 thirdForm = new Form3();
            thirdForm.Show();
            
        }

        private void button28_Click(object sender, EventArgs e)
        {
            Form1.ActiveForm.Hide();
            Form7 sevenForm = new Form7();
            sevenForm.Show();
        }
       
    }
}
