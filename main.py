# public static void main(String[] args) {
		
# 		int []cutPart= {8,12,22,30,32};
# 		int []cutModal= {100,120,140};
# 		int resultindex=0;
		
# 		for(int index=0;index<cutModal.length;index++) {
# 			for(int x=0; x<cutPart[0];x++ ) {
# 				for (int a = 0; a <5; a++) {
# 					for (int b = 0; b < 5; b++) {
# 						for (int c = 0; c < 7; c++) {
# 							for (int d = 0; d < 12; d++) {
# 								for (int e = 0; e < 18; e++) {
# 									if (32 * a + 30 * b + 22 * c + 12 * d + 8 * e == cutModal[index]-x) {
# 										resultindex++;
# 										System.out.println(resultindex+") "+"amount of 32cm = " + a + ", amount of 30 cm = " + b + ", amount of 22 cm = " + c + ", amount of 12 cm = " + d + ", amount of 8 cm = " + e+ " Trim="+(x)+" for the modal "+cutModal[index]+" cm");                        
# 										break;
# 	                            	}
# 	                        	}
# 	                    	}
# 	                	}
# 	            	}
# 	        	}
# 			}
# 		}	
# 	}

def main():
		cutPart = [8, 12, 22, 30, 32]
		cutModal = [100, 120, 140]
		resultindex = 0

		for index in range(len(cutModal)):
			for x in range(cutPart[0]):
				for a in range(5):
					for b in range(5):
						for c in range(7):
							for d in range(12):
								for e in range(18):
									if 32 * a + 30 * b + 22 * c + 12 * d + 8 * e == cutModal[index] - x:
										resultindex += 1
										print(f"{resultindex}) amount of 32cm = {a}, amount of 30 cm = {b}, amount of 22 cm = {c}, amount of 12 cm = {d}, amount of 8 cm = {e} Trim={x} for the modal {cutModal[index]} cm")
										break

main()