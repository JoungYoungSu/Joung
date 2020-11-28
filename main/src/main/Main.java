package main;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	/* 백 준 1 0 9 9 6 번 - 별 찍 기 2 1*/
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int num = Integer.parseInt(br.readLine().trim()); 
		
		for(int i = 1 ; i <= num ; i++) {
			if (i % 2 == 1) bw.write("*");
			if (i % 2 == 0) {
				bw.write(" *");
				bw.write("\n");
			} else {
				bw.write("\n");
			}
		}
		
		br.close();
		bw.flush();
	}
}

