using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace texto_enriquecido2
{
    public partial class Hijos : Form
    {
        public Hijos()
        {
            InitializeComponent();            
        }

        private void cortarToolStripButton_Click(object sender, EventArgs e)
        {
            caja_texto.Cut();
        }

        private void pegarToolStripButton_Click(object sender, EventArgs e)
        {
            caja_texto.Paste();
        }

        private void copiarToolStripButton_Click(object sender, EventArgs e)
        {
            caja_texto.Copy();
        }

        private void toolStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void toolStripButtonalignleft_Click(object sender, EventArgs e)
        {
            caja_texto.SelectionAlignment = HorizontalAlignment.Left;
        }

        private void toolStripButtonaligncenter_Click(object sender, EventArgs e)
        {
            caja_texto.SelectionAlignment = HorizontalAlignment.Center;
        }

        private void toolStripButtonalignright_Click(object sender, EventArgs e)
        {
            caja_texto.SelectionAlignment = HorizontalAlignment.Right;
        }

        private void toolStripButtonitalic_Click(object sender, EventArgs e)
        {
            String nombreFuente = caja_texto.Font.Name;
            float tamanoFuente = caja_texto.Font.Size;
            if (caja_texto.SelectionFont.Italic == false)
            {
                if (caja_texto.SelectionFont.Underline == true & caja_texto.SelectionFont.Bold == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic | FontStyle.Bold | FontStyle.Underline);
                }
                else if (caja_texto.SelectionFont.Underline == true & caja_texto.SelectionFont.Bold == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic | FontStyle.Underline);
                }
                else if (caja_texto.SelectionFont.Underline == false & caja_texto.SelectionFont.Bold == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic);
                }
                else if (caja_texto.SelectionFont.Underline == false & caja_texto.SelectionFont.Bold == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Bold | FontStyle.Italic);
                }
            }
            else
            {
                if (caja_texto.SelectionFont.Underline == true & caja_texto.SelectionFont.Bold == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Underline | FontStyle.Bold);
                }
                else if (caja_texto.SelectionFont.Underline == false & caja_texto.SelectionFont.Bold == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Bold);
                }
                else if (caja_texto.SelectionFont.Underline == true & caja_texto.SelectionFont.Bold == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Underline);
                }
                else
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Regular);
                }
            }
        }

        private void toolStripButtonbold_Click(object sender, EventArgs e)
        {
            String nombreFuente = caja_texto.Font.Name;
            float tamanoFuente = caja_texto.Font.Size;
            if (caja_texto.SelectionFont.Bold == false)
            {
                if (caja_texto.SelectionFont.Italic == true & caja_texto.SelectionFont.Underline == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic | FontStyle.Bold | FontStyle.Underline);
                }
                else if (caja_texto.SelectionFont.Italic == true & caja_texto.SelectionFont.Underline == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic | FontStyle.Bold);
                }
                else if (caja_texto.SelectionFont.Italic == false & caja_texto.SelectionFont.Bold == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Bold);
                }
                else if (caja_texto.SelectionFont.Italic == false & caja_texto.SelectionFont.Underline == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Bold | FontStyle.Underline);
                }
            }
            else
            {
                if (caja_texto.SelectionFont.Italic == true & caja_texto.SelectionFont.Underline == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic | FontStyle.Underline);
                }
                else if (caja_texto.SelectionFont.Italic == false & caja_texto.SelectionFont.Underline == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Underline);
                }
                else if (caja_texto.SelectionFont.Italic == true & caja_texto.SelectionFont.Underline == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic);
                }
                else
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Regular);
                }
            }
        }

        private void toolStripButtonunderline_Click(object sender, EventArgs e)
        {

            String nombreFuente = caja_texto.Font.Name;
            float tamanoFuente = caja_texto.Font.Size;
            if (caja_texto.SelectionFont.Underline == false)
            {
                if (caja_texto.SelectionFont.Italic == true & caja_texto.SelectionFont.Bold == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic | FontStyle.Bold | FontStyle.Underline);
                }
                else if (caja_texto.SelectionFont.Italic == true & caja_texto.SelectionFont.Bold == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic | FontStyle.Underline);
                }
                else if (caja_texto.SelectionFont.Italic == false & caja_texto.SelectionFont.Bold == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Underline);
                }
                else if (caja_texto.SelectionFont.Italic == false & caja_texto.SelectionFont.Bold == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Bold | FontStyle.Underline);
                }
            }
            else
            {
                if (caja_texto.SelectionFont.Italic == true & caja_texto.SelectionFont.Bold == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic | FontStyle.Bold);
                }
                else if (caja_texto.SelectionFont.Italic == false & caja_texto.SelectionFont.Bold == true)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Bold);
                }
                else if (caja_texto.SelectionFont.Italic == true & caja_texto.SelectionFont.Bold == false)
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Italic);
                }
                else
                {
                    caja_texto.SelectionFont = new Font(nombreFuente, tamanoFuente, FontStyle.Regular);
                }
            }
        }

        private void toolStripButtonbackgroundcolor_Click(object sender, EventArgs e)
        {
            ColorDialog colorDialog1 = new ColorDialog();

            colorDialog1.Color = caja_texto.SelectionBackColor;

            if (colorDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK &&
               colorDialog1.Color != caja_texto.SelectionBackColor)
            {
                caja_texto.SelectionBackColor = colorDialog1.Color;
            }
        }

        private void TSBundo_Click(object sender, EventArgs e)
        {
            caja_texto.Undo();
        }

        private void TSBredo_Click(object sender, EventArgs e)
        {
            caja_texto.Redo();
        }

        private void toolStripButtonFontDialog_Click(object sender, EventArgs e)
        {
            FontDialog fontDialog1 = new FontDialog();

            fontDialog1.ShowColor = true;

            fontDialog1.Font = caja_texto.SelectionFont;
            fontDialog1.Color = caja_texto.SelectionColor;

            if (fontDialog1.ShowDialog() != DialogResult.Cancel)
            {
                caja_texto.SelectionFont = fontDialog1.Font;
                caja_texto.SelectionColor = fontDialog1.Color;
            }

        }

        private void toolStripButtonColor_Click(object sender, EventArgs e)
        {
            ColorDialog colorDialog1 = new ColorDialog();

            colorDialog1.Color = caja_texto.SelectionColor;

            if (colorDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK &&
               colorDialog1.Color != caja_texto.SelectionColor)
            {
                caja_texto.SelectionColor = colorDialog1.Color;
            }
        }

        private void toolStripButtonAddImage_Click(object sender, EventArgs e)
        {

            FileDialog fDialog = new OpenFileDialog();
            fDialog.CheckFileExists = true;
            fDialog.CheckPathExists = true;
            fDialog.RestoreDirectory = true;
            fDialog.Title = "Choose file to import";
            if (fDialog.ShowDialog() == DialogResult.OK)
            {
                string lstrFile = fDialog.FileName;
                Bitmap myBitmap = new Bitmap(lstrFile);
                // Copy the bitmap to the clipboard.
                Clipboard.SetDataObject(myBitmap);
                DataFormats.Format format = DataFormats.GetFormat(DataFormats.Bitmap);

                caja_texto.Paste(format);
            }
        }

    }
}
