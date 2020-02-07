package sopa;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.GraphicsConfiguration;
import java.awt.GridLayout;
import java.awt.HeadlessException;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Ventana extends JFrame implements ActionListener {

	Busqueda obj = new Busqueda();

	JPanel panel1;
	JLabel titulo;
	JPanel R_titulo;
	JPanel Matriz_sopa;
	JPanel R_boton;
	JButton boton;
	JTextField[][] letras;

	JPanel panel2;
	JPanel R_datos;
	JPanel R_palabras;
	JLabel numeros_clave;
	JLabel tiempo_total;
	JTextField caja_tiempo_total;
	JLabel[] labels = new JLabel[28];
	JTextField[] textos = new JTextField[24];

	public Ventana(String title) throws HeadlessException {
		super(title);
		setSize(1030, 530);
		setLayout(null);
		setResizable(false);

		// Llenado
		panel1 = new JPanel();
		panel2 = new JPanel();
		R_titulo = new JPanel();
		titulo = new JLabel("SOPA DE LETRAS");
		Matriz_sopa = new JPanel();
		R_boton = new JPanel();
		boton = new JButton("INICIAR EJECUCION DEL PROGRAMA");
		R_datos = new JPanel();
		numeros_clave = new JLabel("NUMEROS CLAVE                                                         ");
		tiempo_total = new JLabel("Tiempo Total:");
		caja_tiempo_total = new JTextField("                                   ");
		R_palabras = new JPanel();
		letras = new JTextField[16][16];

		add(panel1);
		add(panel2);

		// config Panel1
		panel1.setBounds(10, 0, 400, 530);
		panel1.setLayout(null);
		panel1.add(R_titulo);
		panel1.add(Matriz_sopa);
		panel1.add(R_boton);

		R_titulo.setBounds(0, 10, 400, 50);
		R_titulo.add(titulo);
		Matriz_sopa.setBounds(0, 60, 400, 400);
		Matriz_sopa.setLayout(new GridLayout(16, 16));

		// JTextFields y  mapeo de sopa

		for (int x = 0; x < 16; x++) {
			for (int y = 0; y < 16; y++) {

				letras[x][y] = new JTextField();
				Matriz_sopa.add(letras[x][y]);
				letras[x][y].setEditable(false);
				letras[x][y].setText(" " + obj.matriz[x][y]);
			}

		}
		
		R_boton.setBounds(0, 460, 400, 450);
		R_boton.add(boton);

		// config panel2
		panel2.setBounds(410, 0, 610, 530);
		panel2.setLayout(null);
		panel2.add(R_datos);
		panel2.add(R_palabras);

		R_datos.setBounds(0, 10, 620, 50);
		R_datos.add(numeros_clave);
		R_datos.add(tiempo_total);
		R_datos.add(caja_tiempo_total);
		R_palabras.setBounds(0, 60, 620, 430);
		// R_palabras.setBackground(Color.MAGENTA);
		R_palabras.setLayout(new GridLayout(13, 4));

		// cajas para los tiempos

		for (int i = 0; i < (textos.length); i++) {
			textos[i] = new JTextField();
		}

		// palabras

		labels[0] = new JLabel("   letra");
		labels[1] = new JLabel("tiempo de busqueda");
		labels[2] = new JLabel("   letra");
		labels[3] = new JLabel("tiempo de busqueda");
		labels[4] = new JLabel("   inteligencia");
		labels[5] = new JLabel("   bioinformatica");
		labels[6] = new JLabel("   pacman");
		labels[7] = new JLabel("   razonamiento");
		labels[8] = new JLabel("   matrix");
		labels[9] = new JLabel("   genetica");
		labels[10] = new JLabel("   aprendizaje");
		labels[11] = new JLabel("   robotica");
		labels[12] = new JLabel("   juegos");
		labels[13] = new JLabel("   turing");
		labels[14] = new JLabel("   prolog");
		labels[15] = new JLabel("   jframe");
		labels[16] = new JLabel("   simulacion");
		labels[17] = new JLabel("   java");
		labels[18] = new JLabel("   skynet");
		labels[19] = new JLabel("   humanidad");
		labels[20] = new JLabel("   busqueda");
		labels[21] = new JLabel("   lisp");
		labels[22] = new JLabel("   logica");
		labels[23] = new JLabel("   pong");
		labels[24] = new JLabel("   nexus");
		labels[25] = new JLabel("   utopia");
		labels[26] = new JLabel("   deckard");
		labels[27] = new JLabel("   atari");

		// llenado de la caja de palabras

		R_palabras.add(labels[0]);
		R_palabras.add(labels[1]);
		R_palabras.add(labels[2]);
		R_palabras.add(labels[3]);
		R_palabras.add(labels[4]);
		R_palabras.add(textos[0]);
		R_palabras.add(labels[5]);
		R_palabras.add(textos[1]);
		R_palabras.add(labels[6]);
		R_palabras.add(textos[2]);
		R_palabras.add(labels[7]);
		R_palabras.add(textos[3]);
		R_palabras.add(labels[8]);
		R_palabras.add(textos[4]);
		R_palabras.add(labels[9]);
		R_palabras.add(textos[5]);
		R_palabras.add(labels[10]);
		R_palabras.add(textos[6]);
		R_palabras.add(labels[11]);
		R_palabras.add(textos[7]);
		R_palabras.add(labels[12]);
		R_palabras.add(textos[8]);
		R_palabras.add(labels[13]);
		R_palabras.add(textos[9]);
		R_palabras.add(labels[14]);
		R_palabras.add(textos[10]);
		R_palabras.add(labels[15]);
		R_palabras.add(textos[11]);
		R_palabras.add(labels[16]);
		R_palabras.add(textos[12]);
		R_palabras.add(labels[17]);
		R_palabras.add(textos[13]);
		R_palabras.add(labels[18]);
		R_palabras.add(textos[14]);
		R_palabras.add(labels[19]);
		R_palabras.add(textos[15]);
		R_palabras.add(labels[20]);
		R_palabras.add(textos[16]);
		R_palabras.add(labels[21]);
		R_palabras.add(textos[17]);
		R_palabras.add(labels[22]);
		R_palabras.add(textos[18]);
		R_palabras.add(labels[23]);
		R_palabras.add(textos[19]);
		R_palabras.add(labels[24]);
		R_palabras.add(textos[20]);
		R_palabras.add(labels[25]);
		R_palabras.add(textos[21]);
		R_palabras.add(labels[26]);
		R_palabras.add(textos[22]);
		R_palabras.add(labels[27]);
		R_palabras.add(textos[23]);

		// EVENTOS

		boton.addActionListener(this);

		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
		setVisible(true);

	}

	@Override
	public void actionPerformed(ActionEvent e) {

		long t_inicial, t_final, t_total;

		if (e.getSource() == boton) {

			// palabra inteligencia

			pintar(2, 1, 12, 1, 1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("inteligencia");
			t_final = System.currentTimeMillis();
			textos[0].setText(obj.tiempo(t_final, t_inicial) + " ms");
			t_total = obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra pacman

			pintar(8, 6, 6, 1, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("pacman");
			t_final = System.currentTimeMillis();
			textos[2].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra matrix

			pintar(8, 15, 6, -1, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("matrix");
			t_final = System.currentTimeMillis();
			textos[4].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra aprendizaje

			pintar(11, 0, 11, -1, 0);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("aprendizaje");
			t_final = System.currentTimeMillis();
			textos[6].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra juegos

			pintar(6, 10, 6, -1, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("juegos");
			t_final = System.currentTimeMillis();
			textos[8].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra prolog

			pintar(1, 15, 6, 1, 0);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("prolog");
			t_final = System.currentTimeMillis();
			textos[10].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra simulacion

			pintar(2, 14, 10, 0, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("simulacion");
			t_final = System.currentTimeMillis();
			textos[12].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra skynet

			pintar(11, 9, 6, 0, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("skynet");
			t_final = System.currentTimeMillis();
			textos[14].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra busqueda

			pintar(0, 15, 8, 0, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("busqueda");
			t_final = System.currentTimeMillis();
			textos[16].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra logica

			pintar(5, 7, 6, -1, 0);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("logica");
			t_final = System.currentTimeMillis();
			textos[18].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra nexus

			pintar(5, 8, 5, -1, 1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("nexus");
			t_final = System.currentTimeMillis();
			textos[20].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra deckard

			pintar(10, 7, 7, -1, 1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("deckard");
			t_final = System.currentTimeMillis();
			textos[22].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra bioinformatica

			pintar(15, 13, 14, 0, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("bioinformatica");
			t_final = System.currentTimeMillis();
			textos[1].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra razonamiento

			pintar(14, 14, 12, 0, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("razonamiento");
			t_final = System.currentTimeMillis();
			textos[3].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra genetica

			pintar(14, 15, 8, -1, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("genetica");
			t_final = System.currentTimeMillis();
			textos[5].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra robotica

			pintar(7, 1, 8, 0, 1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("robotica");
			t_final = System.currentTimeMillis();
			textos[7].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra turing

			pintar(7, 5, 6, 1, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("turing");
			t_final = System.currentTimeMillis();
			textos[9].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra jframe

			pintar(0, 4, 6, 1, 0);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("jframe");
			t_final = System.currentTimeMillis();
			textos[11].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra java

			pintar(6, 10, 4, 1, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("java");
			t_final = System.currentTimeMillis();
			textos[13].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra humanidad

			pintar(12, 9, 9, 0, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("humanidad");
			t_final = System.currentTimeMillis();
			textos[15].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra lisp

			pintar(9, 12, 4, 1, 1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("lisp");
			t_final = System.currentTimeMillis();
			textos[17].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra pong

			pintar(8, 5, 4, 1, -1);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("pong");
			t_final = System.currentTimeMillis();
			textos[19].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra utopia

			pintar(9, 2, 6, -1, 0);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("utopia");
			t_final = System.currentTimeMillis();
			textos[21].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			// palabra atari

			pintar(5, 13, 5, 1, 0);
			t_inicial = System.currentTimeMillis();
			obj.buscarpalabra("atari");
			t_final = System.currentTimeMillis();
			textos[23].setText((obj.tiempo(t_final, t_inicial) + " ms"));
			t_total = t_total + obj.tiempo(t_final, t_inicial);
			JOptionPane.showMessageDialog(panel2, "Palabra Encontrada");

			caja_tiempo_total.setText((t_total + " ms"));
			JOptionPane.showMessageDialog(panel2, "Se han encontrado todas las palabras en " + t_total + " ms");
			

			// limpiar grafico al terminar
			for (int i = 0; i < textos.length; i++) {
				textos[i].setText(" ");
			}

			for (int i = 0; i < letras.length; i++) {
				for (int j = 0; j < letras.length; j++) {
					letras[i][j].setBackground(null);
					letras[i][j].setForeground(Color.BLACK);
				}
			}

			caja_tiempo_total.setText(" ");
		}

	}

	// pinta las palabras en la matriz de colores
	public void pintar(int fila, int columna, int numeroCaracteres, int moverEnFila, int moverEnColumna) {

		Random r = new Random();
		Color cambiarColor = new Color(r.nextInt(256), r.nextInt(256), r.nextInt(256));
		int recorrido = 0;
		while ((recorrido < numeroCaracteres) && (fila < obj.matriz.length && columna < obj.matriz.length)
				&& (fila > -1 && columna > -1)) {
			letras[fila][columna].setBackground(cambiarColor);
			letras[fila][columna].setForeground(Color.WHITE);
			fila = fila + moverEnFila;
			columna = columna + moverEnColumna;
			recorrido++;
		}
	}

}