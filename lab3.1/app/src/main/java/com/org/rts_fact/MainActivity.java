package com.org.rts_fact;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private Factorizator factorizator;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        factorizator = new Factorizator();
    }

    public void factorize(View view) {
        EditText editText = findViewById(R.id.editText2);
        TextView tvr1 = findViewById(R.id.tVr1);
        TextView tvr2 = findViewById(R.id.tVr2);
        TextView tvtime = findViewById(R.id.tVtime);
        long[] values;
        values = factorizator.factor(Long.parseLong(editText.getText().toString()));
        tvr1.setText(String.valueOf(values[0]));
        tvr2.setText(String.valueOf(values[1]));
        tvtime.setText(String.valueOf(values[2]));
    }
}
