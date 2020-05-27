package com.org.rts_fact;

import android.app.AlertDialog;
import android.content.DialogInterface;

class Factorizator {
    Long tsLong;
    long[] factor(long N) {
        tsLong = System.currentTimeMillis();
        long a = (long) Math.ceil(Math.sqrt(N));
        long b2 = a * a - N;
	int i = 0;
        while (!isSquare(b2)) {
            a++;
	    i++;
            b2 = a * a - N;
        }
	System.out.println("Number of iterations: " + i);
        long r1 = a - (long)Math.sqrt(b2);
        long r2 = N / r1;

	new AlertDialog.Builder(MainActivity.this)
                    .setTitle("Finished successfully")
                    .setMessage(String.format("iterations: %s", i))
                    .setCancelable(true)
                    .setPositiveButton("ok", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            dialog.cancel();
                        }
                    }).show();
        return new long[]{r1, r2, System.currentTimeMillis() - tsLong};
    }

    /** function to check if N is a perfect square or not **/
    private boolean isSquare(long N) {
        long sqr = (long) Math.sqrt(N);
        return sqr * sqr == N || (sqr + 1) * (sqr + 1) == N;
    }
}
