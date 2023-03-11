import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from '../styles/Home.module.css'
import Hero from '../components/Hero/Hero'
import Intro from '../components/Intro/Intro'
import Script from 'next/script'


const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Head>
        <title>Create Next App</title>
        <meta name="Tickets Booking" content="Get your tickets for the next big event" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
          <Hero />
          <Intro />
      </main>
      <Script src='https://kit.fontawesome.com/4ef8c63dd7.js' />
    </>
  )
}
