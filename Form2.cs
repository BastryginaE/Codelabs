using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Media;

namespace LanguageTutor
{
    public partial class Form2 : Form
    {
        public static int k;
        public Form2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form2.ActiveForm.Hide();
            Form1 firstForm = new Form1();
            firstForm.Show();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
          
            
                switch (Form1.p)
                {
                    case 1: {
                        button2.Visible = true;
                        button3.Visible = true;
                        button4.Visible = true;
                        button5.Visible = true;
                        button6.Visible = true;
                        button7.Visible = true;
                richTextBox1.Text = "Aa";
                button2.Text = "[æ] cat";
                button3.Text = "[ei] way";
                button4.Text = "[ɑ:] car";
                button5.Text = "[Ͻ:] ball";
                button6.Text = "[ɑ] glass";
                button7.Text = "[ei] lake";
                k = 1;
                break;}
                    case 2:
                        {
                            button4.Visible = true;
                            richTextBox1.Text = "Bb";
                            button4.Text = "[b] bat";
                            k = 2;
                            break;
                        }
                    case 4:
                        {
                            button3.Visible = true;
                            button5.Visible = true;
                            richTextBox1.Text = "Сс";
                            button3.Text = "[k] candle";
                            button5.Text = "[s] cent";
                            k = 3;
                            break;
                        }
                    case 5:
                        {
                            button4.Visible = true;
                            richTextBox1.Text = "Dd";
                            button4.Text = "[d] dog";
                            k = 4;
                            break;
                        }
                    case 6:
                        {
                            button2.Visible = true;
                            button3.Visible = true;
                            button4.Visible = true;
                            button5.Visible = true;
                            button6.Visible = true;
                            richTextBox1.Text = "Ee";
                            button2.Text = "[æ] cat";
                            button3.Text = "[ei] way";
                            button4.Text = "[ɑ:] car";
                            button5.Text = "[ǝ:] servant";
                            button6.Text = "[-] pipe";
                            k = 5;
                            break;
                        }
                    case 7:
                        {
                            button4.Visible = true;
                            richTextBox1.Text = "Ff";
                            button4.Text = "[f] flag";
                            k = 6;
                            break;
                        }
                    case 8:
                        {
                            button3.Visible = true;
                            button5.Visible = true;
                            richTextBox1.Text = "Gg";
                            button3.Text = "[g] goose";
                            button5.Text = "[ʤ] gym";
                            k = 7;
                            break;
                        }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            switch (k)
            {
                case 1:
                    {
                        pictureBox1.Image = Image.FromFile("a1cat.jpg");
                        richTextBox2.Visible = true;
                        StreamReader sr = new StreamReader("a1.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox2.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"cat.wav");
                        Sd.Play();
                        break;
                    }
                case 5:
                    {
                        pictureBox1.Image = Image.FromFile("e1egg.jpg");
                        richTextBox2.Visible = true;
                        StreamReader sr = new StreamReader("a1.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox2.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"egg.wav");
                        Sd.Play();
                        break;
                    }
               
            }
           
        }

        private void button3_Click(object sender, EventArgs e)
        {
            switch (k)
            {
                case 1:
                    {
                        pictureBox2.Image = Image.FromFile("a2way.jpg");
                        richTextBox3.Visible = true;
                        StreamReader sr = new StreamReader("a2.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox3.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"way.wav");
                        Sd.Play();
                        break;
                    }
                case 3:
                    {
                        pictureBox2.Image = Image.FromFile("c1candle.jpg");
                        richTextBox3.Visible = true;
                        StreamReader sr = new StreamReader("c1.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox3.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"candle.wav");
                        Sd.Play();
                        break;
                    }
                case 5:
                    {
                        pictureBox2.Image = Image.FromFile("e2bee.jpg");
                        richTextBox3.Visible = true;
                        StreamReader sr = new StreamReader("a2.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox3.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"way.wav");
                        Sd.Play();
                        break;
                    }
                case 7:
                    {
                        pictureBox2.Image = Image.FromFile("g1goose.jpg");
                        richTextBox3.Visible = true;
                        StreamReader sr = new StreamReader("g1.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox3.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"goose.wav");
                        Sd.Play();
                        break;
                    }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            switch (k)
            {
                case 1:
                    {
                        pictureBox3.Image = Image.FromFile("a3car.jpg");
                        richTextBox4.Visible = true;
                        StreamReader sr = new StreamReader("a3.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox4.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"car.wav");
                        Sd.Play();
                        break;
                    }
                
                case 2:
                    {
                        pictureBox3.Image = Image.FromFile("b_bat.jpg");
                        richTextBox4.Visible = true;
                        StreamReader sr = new StreamReader("b.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox4.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"bat.wav");
                        Sd.Play();
                        break;
                    }
                case 4:
                    {
                        pictureBox3.Image = Image.FromFile("d_dog.jpg");
                        richTextBox4.Visible = true;
                        StreamReader sr = new StreamReader("d.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox4.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"dog.wav");
                        Sd.Play();
                        break;
                    }
                case 5:
                    {
                        pictureBox3.Image = Image.FromFile("e3scene.jpg");
                        richTextBox4.Visible = true;
                        StreamReader sr = new StreamReader("a3.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox4.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"car.wav");
                        Sd.Play();
                        break;
                    }
                case 6:
                    {
                        pictureBox3.Image = Image.FromFile("f_flag.jpg");
                        richTextBox4.Visible = true;
                        StreamReader sr = new StreamReader("f.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox4.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"flag.wav");
                        Sd.Play();
                        break;
                    }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            switch (k)
            {
                case 1:
                    {
                        pictureBox4.Image = Image.FromFile("a4ball.jpg");
                        richTextBox5.Visible = true;
                        StreamReader sr = new StreamReader("a4.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox5.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"ball.wav");
                        Sd.Play();
                        break;
                    }
                case 3:
                    {
                        pictureBox4.Image = Image.FromFile("c2cent.jpg");
                        richTextBox5.Visible = true;
                        StreamReader sr = new StreamReader("c2.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox5.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"cent.wav");
                        Sd.Play();
                        break;
                    }
                case 5:
                    {
                        pictureBox4.Image = Image.FromFile("e4servant.jpg");
                        richTextBox5.Visible = true;
                        StreamReader sr = new StreamReader("e4.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox5.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"ball.wav");
                        Sd.Play();
                        break;
                    }
                case 7:
                    {
                        pictureBox4.Image = Image.FromFile("g2gym.jpg");
                        richTextBox5.Visible = true;
                        StreamReader sr = new StreamReader("g2.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox5.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"gym.wav");
                        Sd.Play();
                        break;
                    }

            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            switch (k)
            {
                case 1:
                    {
                        pictureBox5.Image = Image.FromFile("a5glass.jpg");
                        richTextBox6.Visible = true;
                        StreamReader sr = new StreamReader("a5.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox6.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"glass.wav");
                        Sd.Play();
                        break;
                    }
                case 5:
                    {
                        pictureBox5.Image = Image.FromFile("e5pipe.jpg");
                        richTextBox6.Visible = true;
                        StreamReader sr = new StreamReader("e5.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox6.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"glass.wav");
                        Sd.Play();
                        break;
                    }
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            switch (k)
            {
                case 1:
                    {
                        pictureBox6.Image = Image.FromFile("a6lake.jpg");
                        richTextBox7.Visible = true;
                        StreamReader sr = new StreamReader("a6.txt", Encoding.UTF8);
                        string text = sr.ReadToEnd();
                        richTextBox7.AppendText(text);
                        SoundPlayer Sd = new SoundPlayer(@"lake.wav");
                        Sd.Play();
                        break;
                    }
            }
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
