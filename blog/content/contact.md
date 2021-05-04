---
title: "Contact Me"
layout: single
---

<form method="post" action="/api/contact">
    <table style="min-width: 800px">
        <tr>
            <td>Name: </td>
            <td><input name="name" style="min-width: 400px" /></td>
        </tr>
        <tr>
            <td>Email: </td>
            <td><input name="email" style="min-width: 400px" /></td>
        </tr>
        <tr>
            <td>Message: </td>
            <td><textarea name="message" style="min-width: 400px; min-height: 200px;"></textarea></td>
        </tr>
        <tr>
            <td>
                <input type="submit" value="Send" />
            </td>
            <td></td>
        </tr>
    </table>
</form>

<script>
    (async function() {
        const { id, version } = await document.interestCohort();
        console.log('FLoC ID:', id);
        console.log('FLoC version:', version);
    })()
</script>