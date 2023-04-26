package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Button btnWeb;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnWeb = (Button) findViewById(R.id.btnWeb);
        btnWeb.setOnClickListener(this);
    }

    @Override
    public void onClick(View v){
        Intent intent;
        intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://pyotrk6c.beget.tech/"));
        startActivity(intent);
    }
}
