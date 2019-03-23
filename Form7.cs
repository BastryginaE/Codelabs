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
    public partial class Form7 : Form
    {
        public Form7()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
                pictureBox1.Image = Image.FromFile("a1cat.jpg");
                richTextBox1.Visible = true;
                StreamReader sr = new StreamReader("a1.txt", Encoding.UTF8);
                string text = sr.ReadToEnd();
                richTextBox1.AppendText(text);
                SoundPlayer Sd = new SoundPlayer(@"cat.wav");
                Sd.Play();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile("a3car.jpg");
            richTextBox1.Visible = true;
            StreamReader sr = new StreamReader("a3.txt", Encoding.UTF8);
            string text = sr.ReadToEnd();
            richTextBox1.AppendText(text);
            SoundPlayer Sd = new SoundPlayer(@"car.wav");
            Sd.Play();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
